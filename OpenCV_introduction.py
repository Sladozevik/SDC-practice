# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 12:49:38 2017

@author: aslado
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

#img = cv2.imread('messi5.jpg',0)
#cv2.imshow('image',img)
#k = cv2.waitKey(0) & 0xFF
#if k == 27:
#    cv2.destroyAllWindows()
#elif k == ord('s'):
#    cv2.imwrite('messigray1.png',img)
#    cv2.destroyAllWindows()
    
img = cv2.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()