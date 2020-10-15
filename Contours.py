import cv2.cv2 as cv2
import numpy as np

img =cv2.imread("sample.jpeg",0)

ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of Contours =" +str(len(contours)))
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()