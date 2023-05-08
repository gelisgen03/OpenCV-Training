import cv2

import numpy as np

img=np.ones((512,512,3),np.uint8)

def draw(event,x,y,flags,param):
    print(x,y)
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(0,0,255),-1)

    
cv2.namedWindow('paint')
cv2.setMouseCallback('paint',draw)

while True:
    cv2.imshow('paint',img)
    if cv2.waitKey(1)& 0xFF ==ord('q'):
        print("Finally")
        break
    
cv2.destroyAllWindows()    