# -*-coding:utf-8-*-
import os
import xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, 'data/test.xlsx')
print(excel_path)

'''使用xlrd 读取excel'''
#创建一个工作簿对象wb，通过wb对象可以得到各个sheet对象（一个excel文件可以有多个sheet，每个sheet就是一张表格）
wb = xlrd.open_workbook(excel_path)
#通过xxx.sheet_by_name()  可返回对应的Sheet对象
sheet1 = wb.sheet_by_name('Sheet1')
print(sheet1)
print(sheet1.name)
#通过xxx.sheet_by_index()  可返回对应的Sheet对象
sheet2 = wb.sheet_by_index(1)
print(sheet2)
print(sheet2.name)
#通过xxx.sheets()  可返回所有Sheet对象的list
all_sheet = wb.sheets()
print(all_sheet)

#通过xxx.sheet_names() 可返回所有Sheet对象名称的list（为一个str类型的列表）
all_sheet_name = wb.sheet_names()
# print(all_sheet_name)

#通过xxx.sheet_by_index(index)  返回指定索引处的Sheet，相当于xxx.sheets().[index]
# sheet_index = wb.sheet_by_index(1)
# print(sheet_index)

#遍历返回的Sheet对象的list
for each_sheet in all_sheet:
    # print(each_sheet)
    print('sheet名称为：', each_sheet.name)



''' 通过Sheet对象可以获取各个单元格，每个单元格是一个Cell对象 '''
sheet = wb.sheet_by_name('Sheet3')
print('表格名称：{},表格总行数：{},表格总列数:{}'.format(sheet.name, sheet.nrows, sheet.ncols))
print(sheet.row(0),type(sheet.row(0)))
print(sheet.row(1))
print(sheet.row(2))
print(sheet.row(3))


