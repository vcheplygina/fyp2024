import cv2
import numpy as np
import matplotlib.pyplot as plt

def detect_atypical_network(image_path, mask_path):
    '''detect atypical network'''
    # load the lesion image
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, 0)
    # prepare the lesion image
    cropped_image = cv2.bitwise_and(image, image, mask=mask) # crop the image using the mask
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    eq = cv2.equalizeHist(gray)
    
    edges = cv2.Canny(eq, 100, 200) # detect edges to find network
    kernel = np.ones((3,3), np.uint8) # dilate edges to make the network more visible
    network = cv2.dilate(edges, kernel, iterations=1)
    
    return network # return the network mask