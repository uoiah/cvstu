# -*- coding: UTF-8 -*-

# 将该代码放置在图片所在目录运行

import os, sys
from rcgnz_digits import reco_it
import xlsxwriter
import cv2


def picCutOP(f_name, xA, yA, xB, yB):
    cutimg = None
    if f_name.endswith('jpg'):
        image = cv2.imread(path + f_name)
        # cutimg = image[125:220, 300:458]
        cutimg = image[yA:yB, xA:xB]
        # print(image.shape)
        # cv2.imshow(f_name, image)
        return cutimg


path = '/Users/haiou/Desktop/cvstu/picop/videoTest/s46-10-t/'
sys.path.append(path)
workbook = xlsxwriter.Workbook('temperature.xlsx')
worksheet = workbook.add_worksheet()

fileList = os.listdir(path)
fileList.sort()
row = 0
col = 0
for f in fileList:
    f_name = str(f)
    print(f_name)
    if f_name.endswith('png') or f_name.endswith('PNG') or f_name.endswith('jpg'):
        img = picCutOP(f_name, 283, 168, 409, 243)
        # print(f_name[:-4])
        r = reco_it(img)
        worksheet.write(row, col, f_name[:-4])
        worksheet.write(row, col+1, r)
        row += 1

workbook.close()

