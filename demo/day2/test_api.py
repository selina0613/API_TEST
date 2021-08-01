import pytest
import requests
import re
import json
import time

from commom.yaml_utils import write_yaml
from commom.yaml_utils import read_yaml

class TestApi:
    # csrf_token = ""
    # access_token = ""   #设置全局变量
    # session = requests.session() #会话

    def test_get_token(self):
        url ="https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": "wx6b11b3efd1cdc290",
            "secret": "106a9c6157c4db5f6029918738f9529d"
        }
        res_get = requests.get(url=url, params=params)
        #把数据组合成dict，并写入yaml文件
        extract_data = {"access_token": res_get.json()['access_token']}
        write_yaml(extract_data)   #
        # print(res_get.status_code)  #返回状态码
        # 取接口返回值的token，把token的值作为一个全局变量(类变量)，类变量通过类名来访问
        # TestApi.access_token = res_get.json()['access_token']    #json提取


    def test_select_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        params = {
            "access_token": read_yaml("access_token")   #读取yaml中key的值
                           }
        res_post = requests.get(url=url, params=params)
        print(res_post.text)

    def test_edit_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token="+read_yaml("access_token")
        value = {"tag": {"id": 4401, "name": "l"+str(int(time.time()))}}
        strs = json.dumps(value)  #把dict格式转换成json字符串
        res_post = requests.post(url=url, data=strs)
        print(res_post.text)
    #
    # def test_file_upload(self):
    #     """文件上传"""
    #     url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token="+read_yaml("access_token")
    #     value = {
    #         "media": open(r"G:\Desktop\banner.png", "rb")   #文件流上传，不能直接传文件路径
    #     }
    #     res_post = requests.post(url=url, files=value)
    #     print(res_post.text)

    def test_phpwind_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = requests.get(url=url)
        result_value = res.text
        # print(result_value)  # 把返回值转化成文本   ，返回的是一个网页，不能直接转换成json格式，否则会报错
        # 使用正则表达式取值  <input type="hidden" name="csrf_token" value="c11b9f78c861e9f6"/><input
        value = re.search('name="csrf_token" value="(.*?)"', result_value)
        # print(value1)   #打印查看是否取到对应的值，如果有match则表示有匹配到，<_sre.SRE_Match object; span=(4033, 4075), match='name="csrf_token" value="068ee16654c6defc"'>
        # print(value.group(1))  # group(0)表示它本身
        # TestApi.csrf_token = value.group(1)  # group(0)表示它本身
        #把数据组合成dict字典并写入yaml文件
        # extract_data = value.group(1)
        extract_data = {"csrf_token": value.group(1)}
        write_yaml(extract_data)

    def test_phpwind_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        args = {
            "username": "msxy",
            "password": "msxy",
            "csrf_token": read_yaml("csrf_token"),
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",   #客户端接收的数据类型
            "X-Requested-with": "XMLHttpRequest"   #异步请求
        }
        res = requests.post(url=url, data=args, headers=headers)
        print(res.text)

# if __name__ == '__main__':
#     pytest.main('-vs')