import cv2
import numpy as np

cam=cv2.VideoCapture(0)
T=cam.isOpened() # True ya da False deger dondurur. 
if not T:
    print("Kamera taninamadi...")
    exit()

while True:
            
    ret,frame=cam.read() #ret=T&F (kamera için), frame =resmi alir
    font=cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frame,"Asim",(10,250),font,8,(250,0,0),2) #Yazi ekleme
    cv2.circle(frame,(50,50),50,(255,0,0),-1) #cember cizme
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Gri'ye çevirmek için (openCV renkleri okurken BGR formatinda okur)
    
    if not ret:
        print("Kamera acilamadi")
        break
    
    cv2.imshow("Kamera",frame) 
    if cv2.waitKey(1)==ord("q"):
        print("Kamera sonlandirildi...")
        break

      
