import cv2 as cv
import numpy as np

img=np.ones((512,512,3))
img[1:64,1:64]=[0,0,255]
img[448:511,448:511]=[0,0,0]
img[1:64,448:511]=[0,255,0]
img[448:511,1:64]=[255,0,0]
cv.imshow('img',img)
cv.waitKey(0)