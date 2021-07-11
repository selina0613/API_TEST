#测试数据转化
import os
from commom.excel_utils import ExcelUtils

current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path, '..', 'test_data/test_case.xlsx')
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