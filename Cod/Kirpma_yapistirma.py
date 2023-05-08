import cv2 
import matplotlib.pyplot as plt

resim=cv2.imread("bayraktar.jpg")

kirp=resim[350:450,350:500]
resim[70:170,400:550]=kirp
resim[400:500,30:180]=kirp
resim[400:500,800:950]=kirp
resim[400:500,600:750]=kirp
cerceve=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT) #cerceve yapma
plt.subplot(121),plt.imshow(resim) 
plt.subplot(122),plt.imshow(cerceve)
plt.show()