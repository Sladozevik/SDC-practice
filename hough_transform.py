# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 22:14:24 2017

@author: aslado
"""

# Do relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

x = 'exit-ramp.jpg'

# Read in and grayscale the image
image = mpimg.imread(x)
gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

# Define a kernel size and apply Gaussian smoothing
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

# Define our parameters for Canny and apply
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Define the Hough transform parameters
# Make a blank the same size as our image to draw on
rho = 1
theta = np.pi/180
threshold = 199
min_line_length = 225
max_line_gap = 20
line_image = np.copy(image)*0 #creating a blank to draw lines on

# Run Hough on edge detected image
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)

# Iterate over the output "lines" and draw lines on the blank
for line in lines:
    for x1,y1,x2,y2 in line:
        x = cv2.line(line_image,(x1,y1),(x2,y2),(0,0,255),10)
        print('line:', x1,y1,x2,y2)
        plt.imshow(x)
        plt.show()

#y1 = line_image.shape[0] / 2 + 90
#print('y1 = ',y1)
#        
# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges)) 

# Draw the lines on the edge image
combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
plt.imshow(combo)
plt.show()
#plt.imshow(color_edges)
#plt.show()

