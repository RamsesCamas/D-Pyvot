import cv2

cam = cv2.VideoCapture(1)
cam.set(3,640)
cam.set(4,480)
cam.set(10,50)


while True:
    success,img = cam.read()
    cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
    cv2.line(img,(0,img.shape[0]),(img.shape[1],0),(0,0,255),3)
    cv2.imshow('WebCam',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break