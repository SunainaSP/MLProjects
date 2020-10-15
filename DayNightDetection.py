import os
import cv2.cv2 as cv
import numpy as np

for img in os.listdir('.'):

    if img.startswith('b') or img.startswith('c'):
        frame = cv.imread(img)
        if np.sum(np.sum(frame))/(frame.shape[0]*frame.shape[1]*frame.shape[2]) > 90.0:
            print("Day")
        else:
            print("Night")

        cv.imshow('New', frame)
        cv.waitKey(0)
