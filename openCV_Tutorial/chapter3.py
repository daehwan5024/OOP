'''
How to crop and Resize Images
'''

import cv2
import numpy as np

img = cv2.imread("Resources/shapes.png")
print(img.shape) #행(height) /열(width)

#https://opencv-python.readthedocs.io/en/latest/doc/10.imageTransformation/imageTransformation.html?highlight=resize#cv2.resize
imgResize = cv2.resize(img,(1000,500)) #width and height
print(imgResize.shape)

imgCropped = img[46:119,352:495] #행 열

cv2.imshow("Image",img)
#cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)