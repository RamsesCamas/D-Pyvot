import cv2

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
cam.set(10,50)


while True:
    success,img = cam.read()
    cv2.imshow('WebCam',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break