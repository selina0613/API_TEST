"""
日志模块logging基础封装及应用
在自动化测试框架中，日志模块的主要用途是记录执行过程中的相关信息，方便框架执行过程中的问题定位
python标准库logging 用作记录日志，默认分为六种日志级别（括号内为对应的数值）
NOTSET(0)  没有设置日志
DEBUG(10)
INFO(20)
WARNING(30)
ERROR(40)
CRITICAL(50)
自定义日志级别时注意不要和默认的日志级别数值相同
logging执行时输出大于等于设置的日志级别的日志信息，如设置日志级别是INFO，则INFO,Warning,ERROR,CRITICAL级别的日志都会输出。
logging模块的使用步骤：
1、使用getLogger获取logger对象
2、设置Hander对象（Fomatter对象，输出到文件；StreamHandler输出到控制台）
3、使用Logger对象或Handler对象设置日志级别
4、设置Formatter对象(日志的打印格式)
"""
"""
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

pip install -r requirements.txt

三、pytest的运行方式
1、main()方式运行
2、命令行方式运行
    pytest -vs
3、通过配置文件pytest.ini运行
不管是main方式运行，还是命令方式运行，都会自动读取这个配置文件区执行
-vs          -v打印详细信息，-s打印调试信息
-n           -n表示多线程运行
--reruns     失败用例重跑
--html=路径   生成html的报告
-m           执行带标记的测试用例

四、改变pytest用例执行顺序
setup:           在每个用例之前执行一次，如：打开浏览器，加载网页
teardown:        在每个用例之后执行一次，如：关闭浏览器
setup_class:     在每个类之前执行一次，如：创建日志对象，创建数据库连接
teardown_class:  在每个类之后执行一次，如：关闭数据库连接，销毁日志对象
如果有10000个用例，其中三个用例需要做前后置。
部分前后置，使用fixtrue装饰器。固件。
方法如下：
@pytest.fixtrue(scope="作用域",params="数据驱动",autouse="自动执行",ids="数据驱动参数名",
                name="给fixtrue作用的函数重命名")
1、scope参数：
function  函数
class   类
module  模块
package/session   会话

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
会话的前后置，一般会结合conftest.py文件一起使用
1、conftest.py单独用于存放fixture固件的配置文件
2、在conftest.py中固件在使用时不需要导包
3、可以有多个conftest.py文件

接口关联（需要把所有的全局变量都集中管理）
通过一个单独的yaml文件管理
接口自动化测试框架封装第一步：接口关联封装

生成漂亮的allure报告
1、官网下载allure
下载后解压保存到e盘，并且需要把bin路径配置到path里面
2、验证allure是否安装成功
allure --version
3、生成allure测试报告
(1)生成临时的json格式的测试报告
addopts = -vs --alluredir ./temps --clean-alluredir
(2)生成html报告
os.system("allure generate ./temps -o .reports --clean") #o表示output输出

"""