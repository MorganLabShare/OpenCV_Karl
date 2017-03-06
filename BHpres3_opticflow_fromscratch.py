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
plotFlow1x=[]
plotFlow1y=[]
plotFlow2x=[]
plotFlow2y=[]
plotTot1x=[0]
plotTot1y=[0]
plotTot2x=[0]
plotTot2y=[0]
#set up the initial frame
previous = cv2.imread(imlist[0])
previous = cv2.cvtColor(previous, cv2.COLOR_BGR2GRAY)

#For later, we will need to have the dimensions ready for calculations
#create sequential array
intRA=[i+1 for i in range(1920)]
#create the adnaus repeats
xRA=intRA
yRA=intRA[0:1080]

plt.ion()
#plot the examples
plotExamples=plt.figure()
ax1=plotExamples.add_subplot(211)
plt.plot(0,0)
ax2=plotExamples.add_subplot(212)
plt.plot(0,0)

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
  cv2.circle(frameColor,(1024,768), 10, (0,255,0), 5)
  cv2.circle(frameColor,(824,568), 10, (255,0,0), 5)

  #put the displacements for the circle locs on a graph
  plotFlow1=np.array(flowRA[1024,768])
  plotFlow2=np.array(flowRA[824,568])
  plotFlow1x.append(plotFlow1[1])
  plotFlow1y.append(plotFlow1[0])
  plotFlow2x.append(plotFlow2[1])
  plotFlow2y.append(plotFlow2[0])
  plotTot1x.append(plotTot1x[-1]+plotFlow1[1])
  plotTot1y.append(plotTot1y[-1]+plotFlow1[0])
  plotTot2x.append(plotTot2x[-1]+plotFlow2[1])
  plotTot2y.append(plotTot2y[-1]+plotFlow2[0])
  
  ax1.clear()
  ax1.plot(range(i+1),plotFlow1y,'g--')
  ax1.plot(range(i+1),plotFlow2y,'b--')
  ax1.plot(range(i+1),plotFlow1x,'g-')
  ax1.plot(range(i+1),plotFlow2x,'b-')
  ax2.clear()
  plt.plot(plotTot1x,plotTot1y,'g-')
  plt.plot(plotTot2x,plotTot2y,'b-')
  #~ plt.plot(range(i+2),plotTot1x,'g-')
  #~ plt.plot(range(i+2),plotTot2x,'b-')
  #plot the figure
  plotExamples.canvas.draw()
  #plotHist.show()

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
