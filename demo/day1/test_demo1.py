# -*-coding:utf-8-*-
"""
day1 ==>第三方模块requests常用方法及response详解
        requests模块之data、json、文件上传传参
        requests之cookie以及session鉴权处理
一、requests库（安装：pip install requests）
请求：
1.requests.get()     get请求，通过params传参
2.requests.post()    post请求，通过data=None，json=None传参
    1、使用data传参：
    参数是dict类型，请求头Content-Type:appliction/x-www-urlencoded,表示通过表单传参
    格式：a=1&b=2
    参数是str类型：Content-Type:text/plain

    重要的请求头：
    Content-Type:  传值的内容的格式
        application/x-www-urlencoded    表单
        multipart/form-data             表单里有上传文件
        text/plain                      表单里有文件上传
        binary                          二进制文件
    Accept：客户端接收的数据格式
    X-Requested-With: 异步请求
    User-Agent ：客户端的用户信息
    Cookie： Cookie信息
    2.使用json传参：
    不管参数是dict或者str，Content-Type：application/json   格式：{"a":1,"b":2}
    总结：
    data传参要么只传键值对的dict，要么只传str
    json传参一般都是dict，可以是键值对也可以是非键值对
3.requests.put()       put请求
4.requests.delete()    delete请求
5.requests.request()   可以发送所有请求
    method:   请求方式
    url:     请求路径
    params:  get方式传参
    data:    post方式传参
    json:    post方式传参
    headers: 请求头
    cookie:  cookie关联
    files:  文件上传

响应：
print(res_get.text)  #把返回值转化成文本
print(res_get.status_code)  #返回状态码
print(res_get.content) #把返回值转化成字节类型数据  返回结果 b 代表字节
print(res_get.json())  #把返回值转化成一个dict对象
print(res_get.url)     #返回url
print(res_get.headers)  #返回请求头
print(res_get.cookies)   #返回cookie信息
print(res_get.encoding)   #返回编码格式
print(res_get.reason)   #返回信息
print(res.request.method) #request包含所有请求数据


pytest框架管理所有测试用例
默认的测试用例规则
1.模块名必须以test_开头或者_test结尾
2.测试类也要以Test开头
3.测试方法必须以test开头

字符串和dict之间的转换：
1、json。load()    把json字符串转换成dict格式
2、json.dumps()   把dict格式转换成json字符串

"""
import pytest, re, json, time
import requests
# res_get = requests.get()
# res_post =requests.post()
# res_put = requests.put()
# res_delete = requests.delete()
# res_req_get = requests.request("get")
# res_req_post = requests.request("get")

class TestApi:
    # def test_get_token(self):
    #
    #     url ="https://api.weixin.qq.com/cgi-bin/token"
    #     params = {
    #         "grant_type": "client_credential",
    #         "appid": "wx6b11b3efd1cdc290",
    #         "secret": "106a9c6157c4db5f6029918738f9529d"
    #     }
    #     res_get = requests.get(url=url, params=params)
    #     print(res_get.status_code)  #返回状态码
    #     print(res_get.text)

    # def test_select_flag(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/tags/get"
    #     params ={"access_token": "47_wPhfRw8w1hmTNV8PS1OXEMw9un2PqFYUlEGKNWjyfLbftA2TWmCtNpES_LlQKgyesmgNsxzLZzpElp9WLC-FKJTG-iZq_UysBjTyhfKRmTSN3ExFtmBGcHD65lf737oJozKjxCYEaSHp7ePwLPChABABFS"}
    #     res_post = requests.get(url=url, params=params)
    #     print(res_post.text)

    # def test_edit_flag(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=47_wPhfRw8w1hmTNV8PS1OXEMw9un2PqFYUlEGKNWjyfLbftA2TWmCtNpES_LlQKgyesmgNsxzLZzpElp9WLC-FKJTG-iZq_UysBjTyhfKRmTSN3ExFtmBGcHD65lf737oJozKjxCYEaSHp7ePwLPChABABFS"
    #     value = {"tag": {"id": 4401, "name": "l"+str(int(time.time()))}}
    #     strs = json.dumps(value)  #把dict格式转换成json字符串
    #     res_post = requests.post(url=url, data=strs)
    #     print(res_post.text)

    def test_file_upload(self):
        """文件上传"""
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=47_wPhfRw8w1hmTNV8PS1OXEMw9un2PqFYUlEGKNWjyfLbftA2TWmCtNpES_LlQKgyesmgNsxzLZzpElp9WLC-FKJTG-iZq_UysBjTyhfKRmTSN3ExFtmBGcHD65lf737oJozKjxCYEaSHp7ePwLPChABABFS"
        value = {
            "media": open(r"G:\Desktop\banner.png", "rb")
        }
        res_post = requests.post(url=url, files=value)
        print(res_post.text)




if __name__ == '__main__':
    pytest.main(['-vs'])    #-vs表示打印详细信息



# url = "http://mall-api.maizuo.com/mall.user.login"
# headers={
#     "Content-Type": "application/json",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept": "application/json, text/plain, */*"
# }
# data ={
#     "account": "15778179490",
#     "password": "e10adc3949ba59abbe56e057f20f883e",
#     "imgkey": "",
# }
# res_post = requests.post(url=url, data=data, headers=headers)
# print(res_post.status_code)
# print(res_post.cookies)
