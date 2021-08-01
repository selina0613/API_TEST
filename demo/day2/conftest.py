import pytest
from commom.yaml_utils import clear_yaml

@pytest.fixture(scope="session",autouse=True)
def execute_database_aql():
    clear_yaml()#每次执行用例前清空yaml里面的文件
    print("在所有请求之前执行一次")
    yield
    print("在所有请求之后执行一次")

