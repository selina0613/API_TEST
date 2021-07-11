#测试数据转化
import os
from commom.excel_utils import ExcelUtils
#from commom import config   #config使用方法一
from commom.localconfig_utils import local_config  #config使用方法二

current_path = os.path.dirname(__file__)
#写法一：
#test_data_path = os.path.join(current_path, '..', 'test_data/test_case.xlsx')
#对应config方法一写法：
#test_data_path = os.path.join(current_path, '..', config.CASE_DATA_PATH)
#对应config方法二写法：
test_data_path = os.path.join(current_path, '..', local_config.CASE_DATA_PATH)

# print(current_path)
# print(test_data_path)

class TestdataUtils():
    def __init__(self, test_data_path=test_data_path):
        self.test_data_path = test_data_path
        self.test_data = ExcelUtils(test_data_path, 'Sheet1').get_sheet_data_by_dict()

    def __get_testcase_data_dict(self):
        test_case_dict = {}
        for row_data in self.test_data:
            test_case_dict.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return test_case_dict

    def get_testcase_data_list(self):
        testcase_list = []
        for k,v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict['case_name'] = k
            one_case_dict['case_info'] = v
            testcase_list.append(one_case_dict)
        return testcase_list



if __name__ == '__main__':
    testdatautils = TestdataUtils()
    # print(testdatautils.get_testcase_data())
    # print(testdatautils.test_data)
    for i in testdatautils.get_testcase_data_list():
        print(i)