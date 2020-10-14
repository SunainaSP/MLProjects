import cv2
img = cv2.imread('Sample2.jpg')
cv2.imshow('Original', img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("New Image Grayscale", gray_img)
cv2.waitKey()

cv2.destroyAllWindows()