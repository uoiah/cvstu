import os, sys
from rcgnz_digits import reco_it
import cv2

def picCutOP(f_name, xA, yA, xB, yB):
    cutimg = None
    if f_name.endswith('jpg'):
        image = cv2.imread(path + f_name)
        cutimg = image[yA:yB, xA:xB]
        return cutimg

path = '/Users/haiou/Desktop/cvstu/picop/videoTest/s46-10-t/'
sys.path.append(path)


cutimg = picCutOP('10.jpg', 282, 168, 409, 243)
cv2.imshow('cutimg', cutimg)
cv2.waitKey(0)

r = reco_it(cutimg)
print(r)