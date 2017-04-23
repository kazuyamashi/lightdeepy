# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

argvs = sys.argv
argc = len(argvs)
if argc	!= 2:
	print "Usage: ./learning_fisher.py input_file"
	quit()

input_file = argvs[1]

img = cv2.imread(input_file)

sharpness = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
ave = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img, -1, kernerl)

median = cv2.medianBlur(img, 5)
gaussian = cv2.GaussianBlur(img,(5,5),0)
averaging = cv2.blur(img, (5,5))
dilation = cv2.dilate(img,kernel,iterations = 1)

cv2.imshow('origin',img),cv2.imshow('cnn',dst)
cv2.waitKey()
cv2.destroyAllWindows() 