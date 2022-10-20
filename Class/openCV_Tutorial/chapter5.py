'''
Warp Prespective/BirdView
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Resources/cards.jpg")

width,height = 250,350
# 좌상 - 좌하 - 우 - 우하
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])

#좌표의 이동점
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.
cv2.circle(img, (111,219), 10, (255,0,0),-1)
cv2.circle(img, (287,188), 10, (0,255,0),-1)
cv2.circle(img, (154,482), 10, (0,0,255),-1)
cv2.circle(img, (352,440), 10, (0,0,0),-1)


matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)

#using matplotlib
plt.subplot(121), plt.imshow(img), plt.title("Image")
plt.subplot(122), plt.imshow(imgOutput), plt.title("Output")
plt.show()

