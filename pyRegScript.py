#!/bin/python

#imports
import cv2
import matplotlib.pyplot as plt
import numpy as np

#set the parameters

#This needs a full path for imread to work
filename='/mnt/morganlab/karlf/pyRegTest/imgs/00500.tif'

#make a surfe object?
#number is the Hessian filter. no clue.
#dir 
#read the file in (requires a full path)
img = cv2.imread(filename)

plt.imshow(img)