import cv2
import numpy as np

def compactness(mask_path):
    '''assesses the compactness of the lesion - irregularity of edges'''
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE) # load mask
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY) # ensure mask is binary
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    
    area = cv2.contourArea(largest_contour)
    perimeter = cv2.arcLength(largest_contour, True)
    
    compactness = (4 * np.pi * area) / (perimeter ** 2)
    
    return compactness