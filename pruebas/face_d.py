import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('imgs/haarcascade_frontalface_default.xml')

img = cv2.imread('imgs/multi_faces.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.putText(img,'Face',(x+(w//2)-10, y + (h//2)-10), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)


cv2.imshow('Face Detection',img)
cv2.waitKey(0)