import os
import pandas
import numpy as np
from glob2 import glob
import datetime
import xlsxwriter as xw
from readcsv import *


def segSearch(dataDirName, segDict):
    row = 1
    for name in glob(dataDirName + '*.CSV'):
        # print('\t', name)
        time = int(name[-10:-4])
        for key,value in segDict.items():
            if time>=key[0] and time < key[1]:
                print(name, ':', key,'-',value)
        print('\t', time)
        row+=1


def dataProcess(dataDirName, div_size, segDict):
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
        
        t = int(name[-10:-4])
        for key,value in segDict.items():
            if t>=key[0] and t<key[1]:
                # print(name, ':', key,'-',value)
                dataFrame = rdcsv(name)
                df = getMeanDF(dataFrame, div_size, value[0], value[1])
                minData = getMinWl(df)
                worksheet.write_row(row, 1, minData)  
        row+=1
        
    workbook.close()
    os.system('cp result.xlsx ' + dataDirName)
    
def main():
    segDict = {(0,123453):(1492,1561),\
                (123453,155023):(1515,1561),\
                (155023,161534):(1538,1561),\
                (161534,162552):(1515,1561),\
                (162552,182208):(1525,1550),\
                (182208,183105):(1515,1546),\
                (183105,210000):(1515,1550)}
    # for key,value in segDict.items():
#         print(key[0], ':', value[0])
    # segSearch('../exp_result/S46-10-1/', segDict)
    dataProcess('../exp_result/S46-10-1/', 8, segDict)
    
if __name__ == '__main__':
    main()
    