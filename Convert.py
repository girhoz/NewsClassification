# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:46:55 2019

@author: IrisCode
"""

     

import glob, os
import xlwt
import xlrd


folders = glob.glob(r"D:\Dataset Berita\*\\")
excelFile =  xlrd.open_workbook('input.xlsx')
sheet = excelFile.sheet_by_index(0)
data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test', cell_overwrite_ok=True)

x = 0
y = 0
for folder in folders :
    x += 1
    files = glob.glob(folder + '*.txt')
    for file in files:
        news = open(file, "r").read()
        sheet.write(y, 0, news)
        sheet.write(y, 1, x)
        y += 1
        
workbook.save('DataSet.xls')

