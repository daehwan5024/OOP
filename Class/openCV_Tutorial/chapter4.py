'''
How to Draw Shapes and Test

'''

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

#print(img)
#img[:]= 255,0,0

#https://opencv-python.readthedocs.io/en/latest/doc/03.drawShape/drawShape.html?highlight=line#goal

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)


cv2.imshow("Image",img)

cv2.waitKey(0)