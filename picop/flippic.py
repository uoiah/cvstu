import os
import cv2
from glob2 import glob


#输出图片到当前目录vidoe文件夹下 
outPutDirName='flip/'
if not os.path.exists(outPutDirName):     #如果文件目录不存在则创建目录     
	os.makedirs(outPutDirName) 
for fn in glob('*.jpg'): #确认文件格式
    img=cv2.imread(fn)
    horizontal_img=cv2.flip(img,0)#选择旋转类型
    horizontal_img=cv2.flip(horizontal_img,1)#选择旋转类型
    '''使用的是flip(src, flipCode[, dst])函数，其中flipCode参数有三个值可以选择：
        当flipCode的值为 1 ：水平翻转；
        当flipCode的值为 0 ：垂直翻转；
        当flipCode的值为 -1 ：水平垂直翻转；
        实际上相当于将图片以中心远点旋转90、180、270度。'''
    splitName=fn.split(".")
    newName=splitName[0]
    cv2.imwrite('flip/' + newName+'.jpg',horizontal_img)