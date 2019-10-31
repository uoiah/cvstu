# -*- coding:utf-8 -*-
# 测试图像切片
import os, sys

import cv2

path = '/Users/haiou/Desktop/cvstu/picop/videoTest/s46-10-t/'
sys.path.append(path)
def picCutOP(f_name, xA, yA, xB, yB):
    cutimg = None
    if f_name.endswith('jpg'):
        image = cv2.imread(path + f_name)
        # cutimg = image[125:220, 300:458]
        cutimg = image[yA:yB, xA:xB]
        # print(image.shape)
        # cv2.imshow(f_name, image)
        return cutimg
        

        
def main():
    cutimg = picCutOP('1.jpg', 283, 168, 410, 243)
    cv2.imshow('cutimg', cutimg)
    cv2.waitKey(0)
    
if(__name__ == '__main__'):
    main()