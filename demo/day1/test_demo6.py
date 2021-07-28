# -*-coding:utf-8-*-
"""通过session让所有用例在同一个会话中"""
import pytest
import requests
import json
import time
import re

class TestApi:
    csrf_token = ""
    session = requests.session()   #获得一个session对象

#需要正则表达式提取（接口关联）
    def test_phpwind_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = TestApi.session.request("get", url=url)
        result_value = res.text
        value = re.search('name="csrf_token" value="(.*?)"', result_value)
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
            "Accept": "application/json, text/javascript, */*; q=0.01",  # 客户端接收的数据类型
            "X-Requested-with": "XMLHttpRequest"  # 异步请求
        }
        res = res = TestApi.session.request("post", url=url, data=args, headers=headers)
        print(res.text)


if __name__ == '__main__':
    pytest.main('-vs')
