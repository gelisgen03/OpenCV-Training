import cv2


cam=cv2.VideoCapture("sleep.mp4")

while cam.isOpened():
    _,frame=cam.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("VIDEO",frame,)

    if cv2.waitKey(1)==ord("q"):
        print("Video Kapatildi...")
        break

cam.release()
cv2.destroyAllWindows()    