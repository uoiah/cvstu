from imutils.perspective import four_point_transform
from imutils import contours
import imutils
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

    # load the example image
    # image = cv2.imread(file_name)
    # print(image.shape[0])

    # pre-process the image by resizing it, converting it to
    # graycale, blurring it, and computing an edge map
    # image = imutils.resize(image, height=300)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(gray)
    # cv2.imshow('img', img)
#     cv2.waitKey(0)
    # img = np.zeros_like(gray)
    # cv2.normalize(gray, img, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    # blurred = cv2.GaussianBlur(img, (5, 5), 0)
    a = 1.5
    img = float(a) * img
    img[img>255] = 255
    img = np.round(img)
    img[img>170] = 255
    img[img<=170] = 0
    img = img.astype(np.uint8)
    # blurred = cv2.GaussianBlur(img, (5, 5), 0)
    # edged = cv2.Canny(blurred, 50, 200, 255)

    thresh = cv2.threshold(img, 0, 255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # cv2.imshow('thresh', thresh)
#     cv2.waitKey(0)

    # loop over each of the digits
    (h1, w1) = thresh.shape
    jg = (int)((w1 * 39/262.5)/2)
    w = (int)((w1 - 2*jg)/3)
    h = h1

    digits = []
    for i in range(3):
        
        roi = thresh[0:h, (i*(w+jg)):w+(i*(w+jg))]
        # cv2.imshow('thresh', roi)
        
        # compute the width and height of each of the 7 segments
        # we are going to examine
        (roiH, roiW) = roi.shape
        print(roiW, roiH)
        (dW, dH) = (int(roiW * 1/4), int(roiH * 1/7))
        dHC = int(roiH * 1/14)

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
            if total / float(area) > 0.5:
                on[i]= 1

        # lookup the digit and draw it on the image
        print(on)
        
        digit = DIGITS_LOOKUP[tuple(on)]
        digits.append(digit)
        # cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
        # cv2.putText(output, str(digit), (x - 10, y - 10),
        #     cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)

    # display the digits
    # outStr = u"{}{}.{} \u00b0C".format(*digits)
    outStr = u"{}{}.{}".format(*digits)
    print(outStr)
    return outStr