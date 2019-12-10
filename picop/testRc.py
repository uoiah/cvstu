import os, sys
from rcgnz_digits import reco_it
import cv2

def picCutOP(f_name, xA, yA, xB, yB):
    cutimg = None
    if f_name.endswith('jpg'):
        image = cv2.imread(path + f_name)
        cutimg = image[yA:yB, xA:xB]
        return cutimg

path = '/Users/haiou/Desktop/exp_result/e-Octadecane-14-1208/videoCut/'
sys.path.append(path)


cutimg = picCutOP('228.jpg', 217, 87, 361, 175)
cv2.imshow('cutimg', cutimg)
cv2.waitKey(0)

# r = reco_it(cutimg)
# print(r)