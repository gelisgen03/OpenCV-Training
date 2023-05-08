import cv2


cam=cv2.VideoCapture(0)

fourcc=cv2.VideoWriter_fourcc(*'XVID')   #('M','J','P','G') Bu da olabilir --- cedec diye adlandirilan bu şey video çektigim için gerekli
out=cv2.VideoWriter("Kayit_Deneme.mp4",fourcc,20.0,(640,480)) #('ad',codec,fps,(boyut1,boyut2)) bu boş bir şablon:videoyu içine yazmak için

while cam.isOpened():
    _,frame=cam.read() #görüntüyü aldik

    out.write(frame) #şablona yazdik
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("Kayit_Deneme_Hsv",hsv)
    cv2.imshow("Kayit_Deneme",frame)
    cv2.imshow("Kayit_Deneme_RGB,",rgb)

    if cv2.waitKey(1)==ord('q'):
        print("Kamera kapatiliyor")
        break

cam.release()
out.release()
cv2.destroyAllWindows()