import cv2
import numpy as np


img = cv2.imread("/home/marzi/Documents/python/images/lena-1.jpg")
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2)






cv2.imshow("original image", img)
cv2.imshow("pyrDown1 image", lr1)
cv2.imshow("pyrDown2 image", lr2)
cv2.imshow("pyrUp 1 image", hr2) 
#this image has bad quality than lr2 because during pyrdown we lise the image info


cv2.waitKey(0)
cv2.destroyAllWindows()