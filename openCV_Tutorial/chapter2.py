'''
5 Must know opencv functions for you.
Gray Scale, Blur, Edge Detection, Dialation and Erosion
https://opencv-python.readthedocs.io/en/latest/
위 사이트 참고
'''
import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

#https://opencv-python.readthedocs.io/en/latest/doc/08.imageProcessing/imageProcessing.html?highlight=cvtcolor#cv2.cvtColor
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#https://opencv-python.readthedocs.io/en/latest/doc/11.imageSmoothing/imageSmoothing.html?highlight=gaussianblur#cv2.GaussianBlur
imgBlur = cv2.GaussianBlur(imgGray,(17,17),0)

#https://opencv-python.readthedocs.io/en/latest/doc/13.imageGradient/imageGradient.html?highlight=canny
imgCanny = cv2.Canny(img,1,200)

#https://opencv-python.readthedocs.io/en/latest/doc/12.imageMorphological/imageMorphological.html?highlight=dilate
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #팽창

imgEroded = cv2.erode(imgDialation,kernel,iterations=1) #침


cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)