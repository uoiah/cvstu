import os
import pandas
import numpy as np
from glob2 import glob
import datetime
import xlsxwriter as xw
from readcsv import *

def dataProcess(dataDirName, div_size, cutFrom, cutTo):
    workbook = xw.Workbook('result.xlsx')
    worksheet = workbook.add_worksheet()
    headings = ['Time','Wavelength','Loss', 'Temperature']
    worksheet.write_row('A1', headings)
    row = 1
    for name in glob(dataDirName + '*.CSV'):
        # print('\t', name)
        time = name[-19:-4]
        dt = datetime.datetime.strptime(time, "%Y%m%d_%H%M%S")
        dtStr = dt.strftime("%Y-%m-%d %H:%M:%S")
        # print('\t', dt)
        worksheet.write(row, 0, dtStr)
        dataFrame = rdcsv(name)
        df = getMeanDF(dataFrame, div_size, cutFrom, cutTo)
        # minData = getMinWlByPolyFit(df, 0, cutFrom, cutTo)
        minData = getMinWl(df)
        worksheet.write_row(row, 1, minData)
        row+=1
    workbook.close()
    os.system('cp result.xlsx ' + dataDirName)
    
def main():
    dataProcess('../../exp_result/c-Octadecane-15-1203/data/', 1, 1555, 1577)
    
if __name__ == '__main__':
    main()
    