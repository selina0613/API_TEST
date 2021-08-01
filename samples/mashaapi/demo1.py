"""
一、requests库
requests.get()     get请求，通过params传参
requests.post()    post请求，通过data=None，json=None传参
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
requests.put()       put请求
requests.delete()    delete请求
requests.request()   可以发送所有请求
    method:   请求方式
    url:     请求路径
    params:  get方式传参
    data:    post方式传参
    json:    post方式传参
    headers: 请求头
    cookie:  cookie关联
    files:  文件上传
"""
