import cv2
import numpy as np
import imutils

def color_seg(choice):
    if choice == 'blue':
        lower_hue = np.array([100,30,30])
        upper_hue = np.array([150,148,255])
    elif choice == 'white':
        lower_hue = np.array([0,0,0])
        upper_hue = np.array([0,0,255])
    elif choice == 'black':
        lower_hue = np.array([0,0,0])
        upper_hue = np.array([50,50,100])
    return lower_hue, upper_hue

cam = cv2.VideoCapture(1)
cam.set(3,640)
cam.set(4,480)
cam.set(10,50)
while True:
    # Take each frame
    success,img = cam.read()
    #frame = cv2.imread('images/road_1.jpg')

    chosen_color = 'black'


    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_gray = np.array([0, 5, 50], np.uint8)
    upper_gray = np.array([179, 50, 255], np.uint8)
    mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)
    img_res = cv2.bitwise_and(img, img, mask = mask_gray)
    # define range of a color in HSV
    #lower_hue, upper_hue = color_seg(chosen_color)


    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_gray, upper_gray)


    cv2.imshow('frame',img)
    #cv2.imshow('mask',mask)
    cv2.imshow('mask',img_res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break