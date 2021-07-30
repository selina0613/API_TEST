# -*-coding:utf-8-*-
"""
#正则表达式取值
value = re.search('name="csrf_token" value="(.*?)"', result_value)
TestApi.csrf_token = value.group(1)

"""
# import pytest
# import requests
# import json
# import time
# import re
#
# class TestApi:
#     csrf_token = ""
#
#     def test_phpwind_start(self):
#         url = "http://47.107.116.139/phpwind/"
#         res = requests.get(url=url)
#         result_value = res.text
#         print(result_value)   #把返回值转化成文本   ，返回的是一个网页，不能直接转换成json格式，否则会报错
#         #使用正则表达式取值  <input type="hidden" name="csrf_token" value="c11b9f78c861e9f6"/><input
#         value = re.search('name="csrf_token" value="(.*?)"', result_value)
#         # print(value)   #打印查看是否取到对应的值，如果有match则表示有匹配到，<_sre.SRE_Match object; span=(4033, 4075), match='name="csrf_token" value="068ee16654c6defc"'>
#         # print(value.group(1))  # group(0)表示它本身
#         TestApi.csrf_token = value.group(1)   #group(0)表示它本身
#
#
# if __name__ == '__main__':
#     pytest.main('-vs')
