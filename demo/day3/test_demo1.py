# -*-coding:utf-8-*-
"""
day3==> @pytest.mark.parameterizes+yaml数据驱动
        接口自动化测试框架请求封装和接口关联封装
        接口自动化框架结合jenkins实现CI持续集成

#一、解决一个接口只有一个用例的问题（数据驱动）
@pytest.mark.parameterizes(args_name,args_value)
args_name:参数名，字符串
args_value:参数值，(list,tuple,字典列表，字典元祖)，有多少个值那么测试用例就执行多少次

第一种用法：
@pytest.mark.parametrize("caseinfo",["用例1“,"用例2"])
def test_get_token(self, caseinfo)
    print(caseinfo)
第二种用法：解包
@pytest.mark.parametrize("name,age",[["小王“,"18"],["小王“,"18"]])
def test_get_token(self, name, age)
    print(name,age)

二、使用yaml来管理接口自动化测试用例
yaml是一种数据格式，主要用于配置文件或编写用例
yaml只有两种数据：
1、键值对：
key value
2、list 用一组横线开头表示（-）
- 账号
- 密码

操作yaml所使用的第三方库不是yaml，而是pyyaml

一个py文件对应多个接口
一般一个接口对应一个yaml文件，yaml文件里面有几十个用例，有正例和反例。
"""
