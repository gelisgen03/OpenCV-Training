import cv2
import numpy as np


kernel=np.ones((5,5),np.uint8) #Bu parametre genişleme miktarini  degistirmekte
image=cv2.imread("erodedilate.png")

erosion=cv2.erode(image,kernel,iterations=1) #Bu yöntem sayesinde kesikli alanlarda bulumnan ufak renk alanları büyütülür
dilation=cv2.dilate(erosion,kernel,iterations=2) #Beyaz alanlar genişlemekte (erotion işleminden sonra)
opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel) #New
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)

cv2.imshow("Original",image)
cv2.imshow("Erode-dilate",dilation)
cv2.imshow("Erode",erosion)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing) #opening in tersi
#cv2.imshow("win with dilation",erosion)#beyazlar kuculdu
cv2.waitKey(0)

