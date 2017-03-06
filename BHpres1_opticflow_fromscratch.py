#!/bin/python

import cv2
import os
import numpy as np
from time import sleep
import matplotlib.pyplot as plt

#########
#Parameters
#stack directory
imdir="/home/friedrichsenk/TestImageStack/"
#what are the stack files?
imgtype='.png'
#outputfilename
outputfile='testout3.txt'
##########

#get a list of the png files in the directory
imlist=[s for s in os.listdir(imdir) if s.endswith(imgtype)]
imlist.sort()
#open the output
output=open(outputfile,"w")
#create empty array for results
totalFlow=[]
#set up the initial frame
previous = cv2.imread(imlist[0])
previous = cv2.cvtColor(previous, cv2.COLOR_BGR2GRAY)

#For later, we will need to have the dimensions ready for calculations
#create sequential array
intRA=[i+1 for i in range(1920)]
#create the adnaus repeats
xRA=intRA
yRA=intRA[0:1080]

#loop through the images in the stack
for i in range(len(imlist)):
  #get the filename
  imfile=imlist[i]
  #open the file
  frame1 = cv2.imread(imfile)
  #~ print(frame1[1024,768])
  #convert it to grayscale; it's already in grayscale
  frame2 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
  #set the final frame
  frame=frame2
  #~ print(frame[1024,768])
  #calculate the OF from the previous frame
  #this returns a list of the xy vectors for each displacement
  flowRA = cv2.calcOpticalFlowFarneback(previous, frame, None \
    ,0.5, 3, 15, 3, 5, 1.1, 0)
  #add that to the results
  totalFlow.append(flowRA)
  #get the test pixel displacement
  testflow=np.array(flowRA[1024,768])
  #get an RGB for making the picture
  frameColor=frame1
  #arrow length multiplier
  arrowMultiplier=3
  for y in yRA[::20]:
    for x in xRA[::20]:
      currFlow=np.array(flowRA[y,x])
      plotarrowtest=cv2.arrowedLine(frameColor,(x,y) \
        ,(int(x+round(currFlow[1])*arrowMultiplier) \
        ,int(y+round(currFlow[0])*arrowMultiplier)) \
        ,(0,0,255),3)

  #add some circles for the points that we will graph.

  #show the images
  cv2.imshow('comb',frameColor)
  k = cv2.waitKey(30) & 0xff
  if k == 27:
    break
 
  #write results for test pixel 
  #~ output.write(np.array_str(flowRA[1024,768]))

  #set the previous to the current frame for next iteration
  previous=frame
output.close()
cv2.destroyAllWindows()

################### TRASH
  #~ sleep(0.5)
  #~ print(flowRA.shape)
  #~ print("flowRAlen")
  #~ print(len(flowRA))
  #~ print(type(flowRA))
  #~ print("flowRA[0]len")
  #~ print(len(flowRA[0]))
  #~ print(type(flowRA[0]))
  #~ print("flowRA[0,0]len")
  #~ print(len(flowRA[0,0]))
  #~ print(type(flowRA[0,0]))
  #~ print(flowRA[0,0,0])
