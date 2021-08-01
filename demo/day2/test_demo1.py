# -*-coding:utf-8-*-
# day2==> pytest框架简介，用例规则，运行方法详解
#         pytest之fixture装饰器以及conftest.py文件
#         pytest实现断言以及结合生成allure测试报告
"""
一、pytest默认的测试用例规则
默认的测试用例规则
1.模块名必须以test_开头或者_test结尾
2.测试类也要以Test开头
3.测试方法必须以test_开头

pytest工作步骤：
1.发现测试用例：从多个py文件里找到测试用例
2.执行测试用例：按一定的顺序执行，并且生成报告
3.判断测试结果：断言
4.生成测试报告：allure

字符串和dict之间的转换：
1、json。load()    把json字符串转换成dict格式
2、json.dumps()   把dict格式转换成json字符串

二、pytest详细介绍
1、pytest是一个成熟的python单元测试框架
2、能够和自动化测试工具，selenium，requests,appium结合实现自动化
3、skip跳过用例，reruns失败用例重跑，多线程
4、pytest和allure生成完美的测试报告
5、可以结合jenkins实现持续集成
6、pytest有很多插件
pytest                本身
pytest-html           生成html报告的插件
pytest-xdist          实现多线程
pytest-ordering       改变测试用例的执行顺序
pytest-rerunfailures  失败用例重跑
allure-pytest         生成allure报告

#批量安装插件，把要安装的插件放到requirements.txt文件中，再使用以下命令安装
pip install -r requirements.txt

三、pytest的运行方式
1、main()方式运行
if __name__ == '__main__':
    pytest.main('-vs')

2、命令行方式运行
    pytest -vs -n --alluredir ./result
3、通过配置文件pytest.ini运行
#可添加多个命令行参数，空格分开
addopts = -vs

-vs          -v打印详细信息，-s打印调试信息
-n           -n表示多线程运行  （例如：-2 表示2个线程，执行多个用例时执行多个线程可节省测试时间）
--reruns     失败用例重跑
--html=路径   生成html的报告
-m           执行带标记的测试用例

#配置收集用例的路径
testpaths=./case

#自定义测试文件命名规则  run.py会只执行自定义的测试文件
python_files = test_*.py

#自定义测试类命名规则，run.py会只执行自定义的测试类
python_classes = Test*

#自定义测试方法命名规则  run.py会只执行自定义的测试方法
python_functions = test_*

不管是main方式运行，还是命令方式运行，都会自动读取这个配置文件区执行
-vs          -v打印详细信息，-s打印调试信息
-n           -n表示多线程运行
--reruns n    失败用例重跑 n表示重跑次数
--html=路径   生成html的报告
-m           执行带标记的测试用例,m后加需要执行的用例

四、改变pytest用例执行顺序
setup:           在每个用例之前执行一次，如：打开浏览器，加载网页
teardown:        在每个用例之后执行一次，如：关闭浏览器
setup_class:     在每个类之前执行一次，如：创建日志对象，创建数据库连接
teardown_class:  在每个类之后执行一次，如：关闭数据库连接，销毁日志对象
如果有10000个用例，其中三个用例需要做前后置。
即部分前后置，使用fixtrue装饰器。固件。
方法如下：
@pytest.fixtrue(scope="作用域",params="数据驱动",autouse="自动执行",ids="数据驱动参数名",
                name="给fixtrue作用的函数重命名")
1、scope参数：
function  函数  每一个函数或方法都会调用
class   类       每个测试类只运行一次
module  模块      每一个.py文件调用一次
package/session   会话级	每次会话只需要运行一次，会话内所有方法及类，模块都共享这个方法

部分用例的前后置
import pytest
@pytest.fixtrue(scope="function")
def execute_database_sql():
    print("数据库查询")
    yield
    print("数据库校验")


class TestMa:
    def test_baili(self):
        print("baili")
    def test_weiwei(self):
        print("weiwei")

#部分类的前后置
@pytest.mark.usefixtures('execute_database_sql')
class TESTAAAI:
    def test_aaa(self):
        print("test_aaa")

#会话session的前后置，一般会结合conftest.py文件一起使用
1、conftest.py单独用于存放fixture固件的配置文件
2、在conftest.py中固件在使用时不需要导包
3、可以有多个conftest.py文件

六、接口关联（需要把所有的全局变量都集中管理）
比较成熟的方案：通过一个单独的yaml文件管理
接口自动化测试框架封装第一步：接口关联封装

七、生成漂亮的allure报告
1、官网下载allure https://github.com/allure-framework/allure2/releases
下载后解压保存到e盘，并且需要把bin路径配置到path里面
2、验证allure是否安装成功
allure --version
3、生成allure测试报告
(1)生成临时的json格式的测试报告
addopts = -vs --alluredir ./temps --clean-alluredir
(2)生成html报告
os.system("allure generate ./temps -o ./report --clean") #o表示output输出
"""
import pytest

class TestDay2Api:

    # def test_day2_01(self):
    #     """
    #     在pytest.ini文件中设置该语句addopts = -vs --reruns 2 可进行失败用例重跑
    #     然后再执行文件run.py文件，--reruns后需要加重跑的次数参数，例如--reruns 2失败后重跑两次
    #     :return:
    #     """
        # print("测试失败用例重跑")
        # assert 1 == 2

    @pytest.mark.smoke
    def test_day2_02(self):
        """
        在pytest.ini文件中设置该语句addopts = -vs -m smoke可进行冒烟测试
        执行文件run.py会执行被@pytest.mark.smoke标记的用例
        :return:
        """
        print("测试冒烟测试用例")

    @pytest.mark.users
    def test_day2_03(self):
        """
        addopts = -vs -m "smoke or users"   执行多个冒烟模块使用 or
        :return:
        """
        print("用户管理模块的冒烟测试用例")
    #
    # @pytest.mark.run(order=2)
    # def test_day2_04(self):
    #     print("test_day2_04 第二个执行 测试修改用例执行顺序的用例")
    #
    # @pytest.mark.run(order=1)
    # def test_day2_05(self):
    #     print("test_day2_05 第一个执行 测试修改用例执行顺序的用例")

    def test_day2_06(self):
        if 1 < 2:
            pytest.skip("pytest.skip (用于函数内，跳过测试用例)")
        print("pytest.skip (用于函数内，跳过测试用例)")

    @pytest.mark.skip
    def test_day2_07(self):
        print("@pytest.mark.skip(用于函数外，跳过测试用例)")

    @pytest.mark.skipif(condition='1<2', reason='用例正常')
    def test_day2_08(self):
        print("@pytest.mark.skipif(用于函数外，条件condition，跳过原因reason='')")

    def test_day2_09(self):
        print("test_day2_09")
