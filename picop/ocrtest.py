import os, sys
import cv2
from PIL import Image
import pytesseract
# import numpy as np
# import pandas
# import xlsxwriter

def picCutOP(f_name, xA, yA, xB, yB):
    cutimg = None
    if f_name.endswith('BMP'):
        image = cv2.imread(path + f_name)
        cutimg = image[yA:yB, xA:xB]
        return cutimg

path = '/Users/haiou/Desktop/exp_result/e-Octadecane-14-1208/pic/'
sys.path.append(path)


cutimg = picCutOP("G20191208_150241.BMP", 301, 47, 374, 64)
cv2.imshow('cutimg', cutimg)
cv2.waitKey(0)
# cv2.imwrite('/Users/haiou/Desktop/1.jpg', cutimg)



# text = pytesseract.image_to_string(Image.open('/Users/haiou/Desktop/1.jpg'), lang='chi_sim')
text = pytesseract.image_to_string(cutimg, lang='snum')
print(text)