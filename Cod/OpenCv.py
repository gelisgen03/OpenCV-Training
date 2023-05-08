import cv2 as cv
import numpy
from matplotlib import pyplot as pt 


resim=cv.imread("kizkulesi.jpg",0)
cv.namedWindow("image",cv.WINDOW_AUTOSIZE)#boyutunu oynayamazsın 'imshow' yaparken koydugun isimler ayni olmali
cv.namedWindow("image2",cv.WINDOW_NORMAL)  #boyutunu oynayabilirsin
cv.imshow("image",resim) #ekranda göstermek icin
cv.imshow("image2",resim)
cv.imshow("Resim",resim)


# pt.imshow(resim)
# pt.xlabel("openCV Denemeleri",loc="center") #grafik kütüphanesi ile resim üzerinde daha rahat oynama yapılabilir
# pt.show()


k=cv.waitKey(0)

if k==27:
    print("Esc tUsuna basildi")
elif k==ord("s"):
    print("s ye basildi ve kaydedildi")
    cv.imwrite("kizkules_siyah.jpg",resim)
else:
    print("Herhangi bir tusla kaydedildi")