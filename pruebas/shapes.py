import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
img2 = cv2.imread('imgs/pimienta.jpg')
print(img.shape)
print(img2.shape)

img[200:300,100:300] = 255,0,0

cv2.line(img2,(0,0),(img2.shape[1],img2.shape[0]),(0,0,255),3)
cv2.line(img2,(0,img2.shape[0]),(img2.shape[1],0),(0,0,255),3)
cv2.rectangle(img,(100,150),(300,350),(0,255,0),2)
cv2.line(img,(100,150),(300,350),(0,0,255),2)
cv2.line(img,(300,150),(100,350),(0,0,255),2)

cv2.circle(img,(400,50),30,(11,107,221),cv2.FILLED)
cv2.circle(img,(400,50),31,(255,255,255),2)

cv2.putText(img2,"SE BUSCA",(100,70),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))


cv2.imshow('imagen', img)
cv2.imshow('pimienta funada', img2)

cv2.waitKey(0)