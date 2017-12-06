import numpy as np
import cv2

img=cv2.imread('wonder_woman.jpg',cv2.IMREAD_GRAYSCALE)    #changed image format to jpg
img1=cv2.imread('photo.jpg',cv2.IMREAD_ANYCOLOR)
cv2.imshow('image', img)
cv2.imshow('image1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()