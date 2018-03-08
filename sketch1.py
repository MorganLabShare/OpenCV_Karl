# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:44:15 2018

@author: karlf
"""

from time import sleep
import cv2
import numpy as np
import os, sys
from matplotlib import pyplot as plt
import pylab as pl

image = cv2.imread('EdgeTest2.tif',0)
#cv2.imshow('image',image)

#plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])
#plt.show()



def auto_canny(image, sigma=0.33):
	# compute the median of the single channel pixel intensities
	v = np.median(image)
 
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
 
	# return the edged image
	return edged


canned = auto_canny(image)

#list of the names
imlist=[]
for i in range(0,20):
    imname='imagesig%i' % i
    immat=auto_canny(image,(i*0.1))
    #print(imname)
    imlistEntry=[imname,immat]
    imlist.append(imlistEntry)
        
#for i in imlist:
#    imcurr=i[1]
#    plt.imshow(imcurr,cmap='gray',interpolation='bicubic')    

a=np.arange(1800,2000)
b=np.arange(1000,1200)

imlist_crp = imlist[:]
for i in imlist_crp:
    curry=i[1]
    i[1]=i[1][np.ix_(a,b)]
    
#for i in imlist_crp:
#    imcurr=i[1]
#    plt.imshow(imcurr,cmap='gray',interpolation='bicubic')    
    
#plt.imshow(canned, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])
#plt.show()

#while True:
#    for i in imlist_crp:
#        imcurr=i[1]
#        titcurr=i[0]
#        cv2.imshow(titcurr,canned)
#        cv2.waitKey(100)

testRegion=image[np.ix_(a,b)]

#plt.imshow(testRegion, cmap='gray')
cv2.imshow('orig',testRegion)

img=None
while True:
    for i in imlist_crp:
        imcurr=i[1]
        if img is None:
            img = pl.imshow(imcurr)
        else:
            img.set_data(imcurr)
        pl.pause(.25)
        pl.draw()
        
#cv2.destroyAllWindows()

