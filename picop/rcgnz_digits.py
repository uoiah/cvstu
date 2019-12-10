# -*- coding: UTF-8 -*-

# from imutils.perspective import four_point_transform
# from imutils import contours
# import imutils
import cv2
import numpy as np

def reco_it(image):
    DIGITS_LOOKUP = {
        (1, 1, 1, 0, 1, 1, 1): 0,
        (0, 0, 1, 0, 0, 1, 0): 1,
        (1, 0, 1, 1, 1, 0, 1): 2,
        (1, 0, 1, 1, 0, 1, 1): 3,
        (0, 1, 1, 1, 0, 1, 0): 4,
        (1, 1, 0, 1, 0, 1, 1): 5,
        (1, 1, 0, 1, 1, 1, 1): 6,
        (1, 0, 1, 0, 0, 1, 0): 7,
        (1, 1, 1, 1, 1, 1, 1): 8,
        (1, 1, 1, 1, 0, 1, 1): 9
    }
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 灰度图片转黑白
    (th22, thresh) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # 黑白翻转
    cv2.bitwise_not(thresh, thresh)

    # cv2.imshow('thresh', thresh)
    # cv2.waitKey(0)

    # loop over each of the digits
    (h1, w1) = thresh.shape
    
    w = (int)(w1 * 32/124)
    jg = (int)(w1 * 14/124)
    h = h1
    digits = []
    for i in range(3):
        roi = thresh[0:h, (i*(w+jg)):w+(i*(w+jg))]
        # cv2.imshow('thresh', roi)
        
        # compute the width and height of each of the 7 segments
        # we are going to examine
        (roiH, roiW) = roi.shape
        print(roiW, roiH)
        (dW, dH) = (int(roiW * 9/32), int(roiH * 9/76))
        dHC = int(roiH * 9/152)

        # define the set of 7 segments
        segments = [
            ((dW, 0), (w-dW, dH)),    # top
            ((0, dH), (dW, h // 2 - dHC)),    # top-left
            ((w - dW, dH), (w, h // 2 - dHC)),    # top-right
            ((dW, (h // 2) - dHC) , (w-dW, (h // 2) + dHC)), # center
            ((0, h // 2 + dHC), (dW, h - dH)),    # bottom-left
            ((w - dW - dW//3, h // 2 + dHC), (w - dW // 2, h - dH)),    # bottom-right
            ((dW, h - dH), (w-dW-dHC, h))    # bottom
        ]
        on = [0] * len(segments)

        # loop over the segments
        for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
            # extract the segment ROI, count the total number of
            # thresholded pixels in the segment, and then compute
            # the area of the segment
            segROI = roi[yA:yB, xA:xB]
            total = cv2.countNonZero(segROI)
            area = (xB - xA) * (yB - yA)
            
            # cv2.imshow('thresh' + str(i), segROI)
#             cv2.waitKey(0)

            # if the total number of non-zero pixels is greater than
            # 50% of the area, mark the segment as "on"
            if total / float(area) > 0.50:
                on[i]= 1

        # lookup the digit and draw it on the image
        print(on)
        
        digit = DIGITS_LOOKUP[tuple(on)]
        digits.append(digit)

    # display the digits
    # outStr = u"{}{}.{} \u00b0C".format(*digits)
    outStr = u"{}{}.{}".format(*digits)
    print(outStr)
    return outStr