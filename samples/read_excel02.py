# {'事件':'学习python编程','步骤序号':'step01','步骤操作':'学习了解','完成情况':'100'}
# {'':'','':'','':'','':''}
# {'':'','':'','':'','':''}
# {'':'','':'','':'','':''}

import os
import xlrd
from commom.excel_utils import ExcelUtils


#excel_path = os.path.join(os.path.dirname(__file__), 'data/test.xlsx')
excel_path = os.path.join(os.path.dirname(__file__), 'data/test1.xlsx')
excelUtils = ExcelUtils(excel_path, 'Sheet1')
print(excelUtils.get_merged_cell_value(3,0))  #获取单元格的值

#方法一（基础方法）：
# print(excelUtils.get_row_count())
# sheet_list = []
# for row in range(1,excelUtils.get_row_count()):  #1表示从第二行获取有效数据，表头数据（第一行）不需要
#     row_dict = {}
#     row_dict['事件'] = excelUtils.get_merged_cell_value(row, 0)
#     row_dict['步骤序号'] = excelUtils.get_merged_cell_value(row, 1)
#     row_dict['步骤操作'] = excelUtils.get_merged_cell_value(row, 2)
#     row_dict['完成情况'] = excelUtils.get_merged_cell_value(row, 3)
#     sheet_list.append( row_dict)
#
# for row in sheet_list:  #使用遍历查看是否把所有数据取出来
#     print( row )
#
#方法二（优化代码）：
all_data_list = []
first_row = excelUtils.sheet.row(0)#获取第一行的数据
print( first_row )
for row in range(1,excelUtils.get_row_count()):
    row_dict = {}
    for col in range(0,excelUtils.get_col_count()):
        row_dict[first_row[col].value] = excelUtils.get_merged_cell_value(row,col)
    all_data_list.append( row_dict)

for row in all_data_list:
    print(row)

