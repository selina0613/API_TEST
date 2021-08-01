import pytest

# @pytest.fixture(scope="function")  #如果加了autouse=True则会执行所有用例的前后置
@pytest.fixture(scope="class")
def execute_database_aql():
    print("数据库查询")
    yield
    print("数据库校验")

@pytest.mark.userfixtures('execute_database_aql')
class TestDemo3Api:
    def test_demo3_01(self):
        print("执行test_demo3_01")

    def test_demo3_02(self, execute_database_aql):
        print("执行test_demo3_02")

class TestDemo2Api2:
    def test_demo3_03(self):
        print("执行test_demo3_03")