import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_image(image_path, mask_path):
    """load the image and its mask"""
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    return image, mask

def detect_blue_white(image, mask):
    """detect blue-white veil areas in the image using the mask"""

    # crop the image using the mask so that we only work with the lesion
    cropped_image = cv2.bitwise_and(image, image, mask=mask)
    
    # convert the cropped image to HSV 
    hsv = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
    
    # define bounds for color detection - HUE | SATURATION | VALUE (brightness)
    lower_blue = np.array([90, 20, 80])
    upper_blue = np.array([150, 150, 150])
    
    # creates a new mask where all pixels fall within the defined bounds
    detected_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    return detected_mask

def coverage_ratio(detected_mask, mask):
    veil_area = np.sum(detected_mask > 0) # total area of the blue-white veil
    total_area = np.sum(mask > 0)
    
    coverage_ratio = round(veil_area / total_area, 4)
    
    return coverage_ratio


def blue_white_veil(image_path, mask_path):
    """calculate the coverage ratio of blue-white veil areas"""
    image, mask = load_image(image_path, mask_path)
    detected_mask = detect_blue_white(image, mask)
    result = coverage_ratio(detected_mask, mask)
    
    return result
