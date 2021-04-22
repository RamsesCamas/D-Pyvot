import cv2
import numpy as np

img = cv2.imread('imgs/ram.jpeg')

kernel = np.ones((2,2),np.uint8)

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(9,9),0)
img_canny = cv2.Canny(img,100,150)
img_dilation = cv2.dilate(img_canny,kernel,iterations=1)
img_eroded = cv2.erode(img_dilation,kernel,iterations=1)

#cv2.imshow('Imagen',img)
#cv2.imshow('Imagen gris',img_gray)
#cv2.imshow('Imagen desenfocada',img_blur)
cv2.imshow('Bordes de imagen',img_canny)
cv2.imshow('Bordes dilatados',img_dilation)
cv2.imshow('Bordes erocionados',img_eroded)

cv2.waitKey(0)