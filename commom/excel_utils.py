#导入模块顺序1.内置模块，2.第三方模块（pip安装的），3.自定义模块
import os
import xlrd

class ExcelUtils():
    #初始化
    def __init__(self,file_path,sheet_name):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()  #整个表格对象

    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    def __get_row_count(self):  #获取总行数
        row_count = self.sheet.nrows
        return row_count

    def __get_col_count(self):   #获取总列数
        col_count = self.sheet.ncols
        return col_count

    def get_cell_value(self, row_index, col_index):#获取表格数据，传入行列索引
        cell_value = self.sheet.cell_value(row_index, col_index)
        return cell_value

    def get_merged_info(self):  #获取表格所有的合并信息
        merged_info = self.sheet.merged_cells
        return merged_info

#取数据
    def get_merged_cell_value(self,row_index, col_index):
        '''既能获取合并单元格的数据,又能获取普通单元格的数据'''
        cell_value = None
        for (rlow, rhigh, clow, chigh) in self.get_merged_info():
            if (row_index >= rlow and row_index < rhigh):
                if (col_index >= clow and col_index < chigh):
                    cell_value = self.get_cell_value(rlow, clow)
                    break  # 防止循环去进行判断出现覆盖的情况
                else:
                    cell_value = self.get_cell_value(row_index, col_index)
            else:
                cell_value = self.get_cell_value(row_index, col_index)
        return cell_value

    def get_sheet_data_by_dict(self):#通过字典方式返回所有数据
        all_data_list = []
        first_row = excelUtils.sheet.row(0)   #获取首行数据
        for row in range(1, self.__get_row_count()):
            row_dict = {}
            for col in range(0, self.__get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            all_data_list.append(row_dict)
        return all_data_list


if __name__ == '__main__':
    current_path = os.path.dirname(__file__) #当前代码路径
    excel_path = os.path.join(current_path, '..', 'samples/data/test.xlsx')
    excelUtils = ExcelUtils(excel_path, 'Sheet1')
    #print(excelUtils.get_merged_cell_value(4,0))