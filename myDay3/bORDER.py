#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:50:35 2024

@author: ai-1
"""

import cv2 as cv
import numpy as np

img=cv.imread('apple.jpg')
x,y,c=img.shape
print(x,y)

m=x/10
m=int(m)
print(m)
img[1:m,1:x]=[0,0,0]
img[511-m:511,1:511]=[0,0,0]

img[1:511,1:m]=[0,0,0]
img[1:511,511-m:512]=[0,0,0]
cv.imshow('img',img)
cv.waitKey(0)