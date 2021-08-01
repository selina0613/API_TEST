# -*-coding:utf-8-*-

import pytest

class TestDemo2Api:
    def setup(self):
        print("在每个测试用例之前执行一次，如：打开浏览器，加载网页")

    def teardown(self):
        print("在每个用例之后执行一次，如：关闭浏览器")

    def setup_class(self):
        print("在每个类之前执行一次，创建日志对象，创建数据库连接")

    def teardown_class(self):
        print("在每个类执行之后执行一次，关闭数据库连接，销毁日志对象")


    def test_demo2_01(self):
        print("test_demo2_01")

    def test_demo2_02(self):
        print("test_demo2_02")