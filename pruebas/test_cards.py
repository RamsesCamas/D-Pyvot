import cv2
import numpy as np

img = cv2.imread('imgs/cards2.jpg')
print(img.shape)
width, height = 250,350
pts1 = np.float32([[517,120],[650,117],[555,305],[685,305]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
img_wrap = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('Cartas',img)
cv2.imshow('Carta',img_wrap)


cv2.waitKey(0)