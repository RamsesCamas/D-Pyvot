import cv2

vid = cv2.VideoCapture('videos/the_world.mp4')

while True:
    success,img = vid.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break