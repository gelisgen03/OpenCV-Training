import cv2
import numpy as np


img=np.zeros((512,512,3),np.uint8)

#cv2.line(img,(0,0),(511,511),(255,0,0),10,2) #çizgi
#cv2.line(img,(511,0),(0,511),(0,0,255),10)

#cv2.rectangle(img,(50,50),(450,250),(255,255,255),4) #içi boş dikdortgen
#cv2.rectangle(img,(450,250),(511,511),(255,255,255),-1) #içi dolu dikdortgen

#cv2.circle(img,(250,120),70,(255,0,0),-1) #içi dolu daire
#cv2.circle(img,(250,250),70,(0,255,0),5)
#cv2.circle(img,(250,380),70,(0,0,255),-1)

font=cv2.FONT_HERSHEY_COMPLEX_SMALL
#cv2.putText(img,"Hello",(10,250),font,6,(255,0,0),2) #Metin



cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()