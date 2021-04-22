import cv2
import numpy as np

img = cv2.imread('imgs/susto.jpg')
print(img.shape) #382,480

img_rs = cv2.resize(img,(640,480))

img_crop = img[0:200,0:200]

cv2.imshow('Imagen',img)
cv2.imshow('Imagen redimensionada',img_rs)
cv2.imshow('Imagen cortada',img_crop)


cv2.waitKey(0)