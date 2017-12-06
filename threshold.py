import cv2
import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('wonder_woman.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('original',img)
cv2.imshow('binary',thresh1)
cv2.waitKey(10000)
cv2.destroyAllWindows()