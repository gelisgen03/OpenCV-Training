import cv2

cam=cv2.VideoCapture(0)

a=cam.isOpened()

if not a:
    print("Kameta Taninamadi")
    exit()
    
while True:
    ret,frame=cam.read()
    if not ret:
        print("Kamera acilamadi")
        break

    cv2.imshow("Live",frame)

    if cv2.waitKey(1)==ord("q"):
        print("Kamera sonlandirildi...")
        break


