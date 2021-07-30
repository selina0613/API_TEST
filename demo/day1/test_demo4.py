# -*-coding:utf-8-*-
"""
同步请求和异步请求的区别:
同步是指：发送方发出数据后，等接收方发回响应以后才发下一个数据包的通讯方式。
异步是指：发送方发出数据后，不等接收方发回响应，接着发送下个数据包的通讯方式。
"""

import pytest
import requests
import json
import time
import re

class TestApi:
    csrf_token = ""

    def test_phpwind_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = requests.get(url=url)
        result_value = res.text
        # print(result_value)  # 把返回值转化成文本   ，返回的是一个网页，不能直接转换成json格式，否则会报错
        # 使用正则表达式取值  <input type="hidden" name="csrf_token" value="c11b9f78c861e9f6"/><input
        value = re.search('name="csrf_token" value="(.*?)"', result_value)
        # print(value)   #打印查看是否取到对应的值，如果有match则表示有匹配到，<_sre.SRE_Match object; span=(4033, 4075), match='name="csrf_token" value="068ee16654c6defc"'>
        # print(value.group(1))  # group(0)表示它本身
        TestApi.csrf_token = value.group(1)  # group(0)表示它本身

    def test_phpwind_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        args = {
            "username": "msxy",
            "password": "msxy",
            "csrf_token": TestApi.csrf_token,
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",   #客户端接收的数据类型
            "X-Requested-with": "XMLHttpRequest"   #异步请求
        }
        res = requests.post(url=url, data=args, headers=headers)
        print(res.text)
        # result_value = res.text
        # print(result_value)   #把返回值转化成文本   ，返回的是一个网页，不能直接转换成json格式，否则会报错
        # #使用正则表达式取值  <input type="hidden" name="csrf_token" value="c11b9f78c861e9f6"/><input
        # value = re.search('name="csrf_token" value="(.*?)"', result_value)
        # # print(value)   #打印查看是否取到对应的值，如果有match则表示有匹配到，<_sre.SRE_Match object; span=(4033, 4075), match='name="csrf_token" value="068ee16654c6defc"'>
        # # print(value.group(1))  # group(0)表示它本身
        # TestApi.csrf_token = value.group(1)   #group(0)表示它本身

#写了run.py文件后可不写main，会通过pytest.ini配置文件去执行所有指定的文件及用例
# if __name__ == '__main__':
#     pytest.main('-vs')

#参数都正确，却还报以下错误
#{"referer":null,"refresh":null,"state":"fail","message":["Sorry, CSRF verification failed(token missing or incorrect),refresh to try again."],"__error":""
#针对报错，所以需要做cookie鉴权