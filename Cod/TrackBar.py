import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)

def f(x):
 pass


cv2.namedWindow('Bars')
cv2.createTrackbar('ON/OFF','Bars',0,1,f)
cv2.createTrackbar('R','Bars',0,250,f)
cv2.createTrackbar('G','Bars',0,250,f)
cv2.createTrackbar('B','Bars',0,250,f)


while(1):
    cv2.imshow('Bars',img)
    swich=cv2.getTrackbarPos('ON/OFF','Bars')

    if cv2.waitKey(1)& 0xFF==27:
       break 
    if swich ==1:
        r=cv2.getTrackbarPos('R','Bars')
        g=cv2.getTrackbarPos('G','Bars')
        b=cv2.getTrackbarPos('B','Bars')
        img[:]=[b,g,r]
    else:
       img[:]=[0,0,0]    
    
       