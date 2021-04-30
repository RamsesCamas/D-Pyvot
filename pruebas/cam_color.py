import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars',640,250)

cv2.createTrackbar('Hue Min','TrackBars',0,179,empty)
cv2.createTrackbar('Hue Max','TrackBars',179,179,empty)
cv2.createTrackbar('Sat Min','TrackBars',65,255,empty)
cv2.createTrackbar('Sat Max','TrackBars',255,255,empty)
cv2.createTrackbar('Val Min','TrackBars',104,255,empty)
cv2.createTrackbar('Val Max','TrackBars',255,255,empty)

cam = cv2.VideoCapture(1)
cam.set(3,640)
cam.set(4,480)
cam.set(10,50)


while True:
    success,img = cam.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('Hue Min','TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max','TrackBars')
    s_min = cv2.getTrackbarPos('Sat Min','TrackBars')
    s_max = cv2.getTrackbarPos('Sat Max','TrackBars')
    v_min = cv2.getTrackbarPos('Val Min','TrackBars')
    v_max = cv2.getTrackbarPos('Val Max','TrackBars')

    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)

    img_col = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow('Detectar color',img)
    cv2.imshow('Img HSV', imgHSV)
    cv2.imshow('Img Mask', mask)
    cv2.imshow('Color', img_col)

    cv2.waitKey(1)
