#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:53:20 2023

@author: vech
"""
import numpy as np
import matplotlib.pyplot as plt

# Import packages for image processing
from skimage import morphology #for measuring things in the masks


#-------------------
# Help functions
#------------------



#Main function to extract features from an image, that calls other functions    
def extract_features(image):
    
    [r,g,b] = get_pixel_rgb(image)

    #Here you need to add more of your custom-made functions for measuring features!

    return np.array([r,g,b], dtype=np.float16)




# Extracts the RGB values at location 100, 100. 
# Example feature, probably not very useful
def get_pixel_rgb(image):

    x_coord = 100
    y_coord = 100

    r = image[x_coord, y_coord, 0]
    g = image[x_coord, y_coord, 1]
    b = image[x_coord, y_coord, 2]

    return r,g,b

