import cv2
import numpy as np

img=cv2.imread("gokkusagi.jpg",0)
ret,tresh=cv2.threshold(img,200,255,cv2.THRESH_BINARY)# sınırı 150 olarak seçtik altında kalanları 0 a (siyah) döndürür üstte kalanlarida beyaza (255)
cv2.imshow("Win",img)
cv2.imshow("Tresh",tresh)
cv2.waitKey(0)
cv2.destroyAllWindows