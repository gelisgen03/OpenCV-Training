import cv2
import numpy as np
import matplotlib.pyplot as plt


img1= cv2.imread("cv.png")
img2= cv2.imread("bayraktar.jpg") 
x,y,z=img1.shape
roi=img2[0:x,0:y]

img1_gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img1_gray,10,255,cv2.THRESH_BINARY) #10 dan yüksek degerleri 255 e donusturdu (siyah-beyaz araliginda) opencv beyaz
mask_inv=cv2.bitwise_not(mask) #0 lar 1, 1 ler 0 oldu (o pencv siyah)
#mask_bg=cv2.bitwise_and(roi,roi,img2=mask_inv)
cv2.imshow("resim",img1)
cv2.imshow("resim2",mask)
cv2.imshow("resim3",mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()


