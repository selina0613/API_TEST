import requests
import pytest
from pprint import pprint
from yamls.read_yaml import read_yaml

class Test_Yaml_Api:

    @pytest.mark.parametrize("caseinfo", read_yaml('register.yaml'))
    def test_register(self, caseinfo):
        print(caseinfo)
        # print(caseinfo['name'])
        # print(caseinfo['request']['url'])
        # print(caseinfo['request']['headers'])
        # print(caseinfo['request']['method'])
        # print(caseinfo['request']['data'])
        # print(caseinfo['validate'])
        res = requests.post(caseinfo['request']['url'], headers=caseinfo['request']['headers'], json=caseinfo['request']['data'])
        pprint(res.json())
        # pprint(res.text)
        # return_value = res.json()

        # #处理断言
        # print(caseinfo['validate'])  #输出结果嵌套字典格式{'eq': {'msg': '手机号为空'}}
        # for key, value in dict(caseinfo['validate']).items():
        #     print(key, value)  #eq {'msg': '密码为空'}
        #     if key =='eq':
        #         for assert_key, assert_value in dict(value).items():
        #             print(assert_key, assert_value) #实际结果，预期结果对比
        #             if return_value[assert_key] == assert_value:
        #                 print('断言成功')
        #             else:
        #                 print('断言失败')
        #     else:
        #         print('不支持的断言方式')


if __name__ == '__main__':
    pytest.main(['-vs'])