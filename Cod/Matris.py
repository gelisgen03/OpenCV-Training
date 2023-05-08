import cv2

import numpy as np

sifir=np.zeros([300,300])
bir=np.ones([300,300])

cv2.namedWindow("Sifir",cv2.WINDOW_NORMAL)
cv2.namedWindow("Bir",cv2.WINDOW_NORMAL)

cv2.imshow("Sifir",sifir)
cv2.imshow("Bir",bir)
cv2.waitKey(0)
cv2.destroyAllWindows()



