# -*-coding:utf-8-*-
"""
必须带请求头，需要正则表达式提取（接口关联），处理cookie鉴权以及session鉴权
cookie是服务器产生的保存在客户端的一小段的文本信息，格式 是字典，键值对
Cookie分类
Session级：保存在内存，当浏览器关闭时自动清除
持久化级：保存在磁盘，只有当失效时间到了才会失效
查看方式
F12查看单一服务器
查看客户端所有的cookie
设置=》高级
Cookie鉴权工作原理
当客户端第一次访问服务器的时候，那么服务器就会生成Cookie信息，然后在第一次响应里面的响应头里面通过Set-Cookie把数据传输给客户端，
客户端从第2-N次访问同一个服务器ip的时候，那么就会自动的在请求头的Cookie里带上这些cookie信息，验证这个原理
"""
# import pytest
# import requests
# import json
# import time
#
# class TestApi:
#     access_token = ""   #设置全局变量
#
#     def test_get_token(self):
#         url ="https://api.weixin.qq.com/cgi-bin/token"
#         params = {
#             "grant_type": "client_credential",
#             "appid": "wx6b11b3efd1cdc290",
#             "secret": "106a9c6157c4db5f6029918738f9529d"
#         }
#         res_get = requests.get(url=url, params=params)
#         print(res_get.status_code)  #返回状态码
#         # 取接口返回值的token，把token的值作为一个全局变量(类变量)，类变量通过类名来访问
#         TestApi.access_token = res_get.json()['access_token']    #json提取
#
#
#     def test_select_flag(self):
#         url = "https://api.weixin.qq.com/cgi-bin/tags/get"
#         params ={
#             "access_token": TestApi.access_token
#                            }
#         res_post = requests.get(url=url, params=params)
#         print(res_post.text)
#
#     def test_edit_flag(self):
#         url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token="+TestApi.access_token
#         value = {"tag": {"id": 4401, "name": "l"+str(int(time.time()))}}
#         strs = json.dumps(value)  #把dict格式转换成json字符串
#         res_post = requests.post(url=url, data=strs)
#         print(res_post.text)
#
#     def test_file_upload(self):
#         """文件上传"""
#         url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token="+TestApi.access_token
#         value = {
#             "media": open(r"G:\Desktop\banner.png", "rb")   #文件流上传，不能直接传文件路径
#         }
#         res_post = requests.post(url=url, files=value)
#         print(res_post.text)
#
# if __name__ == '__main__':
#     pytest.main('-vs')