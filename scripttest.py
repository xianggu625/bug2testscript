#coding=utf8
# 导入xlrd模块
import xlrd
from xlutils.copy import copy
import unittest
from project import bug2report

class checkbug2report(unittest.TestCase):
        def setUp(self):
            #设置文件名和路径
            fname = 'bug2report.xlsx'
            # 打开文件
            filename = xlrd.open_workbook(fname)
            #获取当前文档的表(得到的是sheet的个数，一个整数）
            self.sheets=filename.nsheets
            self.sheet1 = filename.sheets()[0]
            self.sheet2 = filename.sheets()[1] 
            # print sheet
            #获取行数
            self.nrows1 = self.sheet1.nrows
            self.nrows2 = self.sheet2.nrows
            '''# 获取列数
            ncols = sheet.ncols
            #获取第一行,第一列数据数据
            cell_value = sheet.cell_value(1,1)
            cell_value1 = sheet.cell(3,0)
             #获取第一行数据
            row_data = sheet.row_values(1)
            #获取第一列,第四行一下的数据
            col_data = sheet.col_values(0,4)
            #获取各行数据
            row_list=[]'''
        def test_ops(self):
            b2r = bug2report()
            for i in range(0,self.nrows1):
                row_datas = self.sheet1.row_values(i)
                #row_list.append(row_datas)
                inputstring = row_datas[0]
                exceptstring =row_datas[1].replace("\t","").strip()
                accutstring = b2r.getElenument(inputstring)
                self.assertEqual(accutstring,exceptstring)
                print(inputstring+" is passing")

        def test_assert(self):
            b2r = bug2report()
            for i in range(0,self.nrows2):
                row_datas = self.sheet2.row_values(i)
                #row_list.append(row_datas)
                inputstring = row_datas[0]
                exceptstring =row_datas[1].replace("\t","").strip()
                accutstring = b2r.myassert(inputstring)[:-1]
                self.assertEqual(accutstring,exceptstring)
                print(inputstring+" is passing")

if __name__=="__main__":
        unittest.main()
                
