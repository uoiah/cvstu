import os, sys
# from rcgnz_digits import reco_it
import cv2

def picCutOP(f_name, xA, yA, xB, yB):
    cutimg = None
    if f_name.endswith('jpg'):
        image = cv2.imread(path + f_name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cutimg = gray[yA:yB, xA:xB]
        (thresh, im_bw) = cv2.threshold(cutimg, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        return im_bw

path = '/Users/haiou/Desktop/exp_result/6-Octadecane-10-1125/videoCut/'
sys.path.append(path)


cutimg = picCutOP('13.jpg', 318, 102, 442, 178)
cv2.imshow('cutimg', cutimg)
cv2.waitKey(0)

# r = reco_it(cutimg)
# print(r)