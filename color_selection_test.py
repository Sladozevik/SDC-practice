# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 22:32:55 2017

@author: aslado
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# read image and print stats
image = mpimg.imread('test.jpg')
#print('This image is:', type(image),'with dimensions', image.shape)

# Grab x and y size and make copy of the image
# Note: alwqys make a copy rather thean simply using '='
ysize = image.shape[0]
xsize = image.shape[1]
color_select = np.copy(image)
line_image = np.copy(image)

# colour check
                    
red_threshold = 205
green_threshold = 0
blue_threshold = 0
rgb_threshold = [red_threshold,green_threshold,blue_threshold]

# Define region of interest
# Keep in mind the origin (x=0, y=0) is in the upper left in image processing
# Note: if you run this code, you'll find these are not sensible values!!
# But you'll get a chance to play with them soon in a quiz

left_bottom = [70,539]
right_bottom = [850,539]
apex = [475,325]

# Fit lines (y=Ax+B) to identify 3 sided region of interest
# np.polyfit( returns the coefficients [A,B]) of the fit
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# Mask pixels below the threshold
#thresholds = (image[:,:,0] ; rgb_threshold[0])\(image[:,:,1] < rgb_threshold[1])\(image[:,:,2] < rgb_threshold[2])
color_thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])

# find the region inside the lines and retunr image
XX, YY = np.meshgrid(np.arange(0,xsize),np.arange(0,ysize))
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))
# Mask color and region selection
color_select[color_thresholds | ~region_thresholds] = [0, 0, 0]
# Color pixels red where both color and region selections met
line_image[~color_thresholds & region_thresholds] = [255, 0, 0]
                    
# Display the image
#plt.imshow(image)
x = [left_bottom[0], right_bottom[0], apex[0], left_bottom[0]]
y = [left_bottom[1], right_bottom[1], apex[1], left_bottom[1]]
plt.plot(x, y, 'b--', lw=4)
plt.imshow(color_select)
plt.imshow(line_image)