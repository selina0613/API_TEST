# -*-coding:utf-8-*-
#网页项目，一般都存在cookie鉴权
import pytest
import requests
import json
import time
import re


class TestApi:
    csrf_token = ""
    php_cookies = ""
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
        #获取cookie
        TestApi.php_cookies = res.cookies


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
            "Accept": "application/json, text/javascript, */*; q=0.01",  # 客户端接收的数据类型
            "X-Requested-with": "XMLHttpRequest"  # 异步请求
        }
        res = requests.post(url=url, data=args, headers=headers,cookies=TestApi.php_cookies)
        print(res.text)
        # result_value = res.text
        # print(result_value)   #把返回值转化成文本   ，返回的是一个网页，不能直接转换成json格式，否则会报错
        # #使用正则表达式取值  <input type="hidden" name="csrf_token" value="c11b9f78c861e9f6"/><input
        # value = re.search('name="csrf_token" value="(.*?)"', result_value)
        # # print(value)   #打印查看是否取到对应的值，如果有match则表示有匹配到，<_sre.SRE_Match object; span=(4033, 4075), match='name="csrf_token" value="068ee16654c6defc"'>
        # # print(value.group(1))  # group(0)表示它本身
        # TestApi.csrf_token = value.group(1)   #group(0)表示它本身


if __name__ == '__main__':
    pytest.main('-vs')

