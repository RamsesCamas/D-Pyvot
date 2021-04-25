import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def get_countours(img):
    countours, hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(img_c,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            aprox = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(f'Num lados: {len(aprox)}')
            obj_cor = len(aprox)
            x,y,w,h = cv2.boundingRect(aprox)

            if obj_cor == 3: shape ='Tri'
            elif obj_cor == 5: shape ='Penta'
            elif obj_cor == 6: shape ='Hexa'
            elif obj_cor == 4: 
                asp_r = w/float(h)
                if asp_r >0.95 and asp_r < 1.05:
                    shape = 'Cuadra'
                else: shape = 'Rect'
            elif obj_cor> 6: shape ='Circle'
            else:
                shape = 'None'
            cv2.rectangle(img_s,(x,y),(x+w,y+h),(0,0,0),5)
            cv2.putText(img_s,shape,(x+(w//2)-50, y + (h//2)-10), cv2.FONT_HERSHEY_COMPLEX,3.5,(0,0,0),2)

path = 'imgs/shapes3.jpg'
img = cv2.imread(path)
img_c = img.copy()
img_s = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

get_countours(imgCanny)

imgs_stacked = stackImages(0.23,([img,imgGray,imgBlur],[img_c,img_s,imgCanny]))
cv2.imshow('Shapes ',imgs_stacked)
cv2.waitKey(0)