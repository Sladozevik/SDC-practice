# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:33:17 2017

@author: aslado
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 # import OpenCV
import numpy as np

# read and convert to gray scale
image = mpimg.imread('exit-ramp.jpg')
plt.imshow(image)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #gray scale conversion

# define kernel size and Gaussian smoothin / blurring
# Note: this step is optional as cv2.Canny() applies a 5x5 Gaussian internally
kernel_size = 3
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size), 0)

# Define Canny Parameters
low_threshold = 100
high_threshold = 200
edges = cv2.Canny(blur_gray, low_threshold, high_threshold) 

# Display the image
#plt.imshow(blur_gray, cmap='gray')
plt.imshow(edges, cmap='Greys_r')
