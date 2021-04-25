import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('imgs/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(1)
cam.set(3,640)
cam.set(4,480)
cam.set(10,50)

while True:
    success,img = cam.read()
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(img,'Rostro',(x+(w//2)-10, y + (h//2)-10), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,252),2)

    cv2.imshow('WebCam',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break