import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_image(path):
    '''loads the mask image'''
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    _, mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return mask

def find_center(mask):
    '''finds the center of the lesion'''
    white_pixels = np.argwhere(mask > 0)
    center_row = np.mean(white_pixels[:, 0]).astype(int)
    center_col = np.mean(white_pixels[:, 1]).astype(int)
    
    return center_row, center_col

def flip_image_centered(mask, axis):
    '''flips the image along its center axis'''
    center_row, center_col = find_center(mask)
    
    if axis == 'vertical':
        image_shifted = np.roll(mask, -center_row, axis=0)
        flipped_image = np.flipud(image_shifted)
        return np.roll(flipped_image, center_row, axis=0)
    elif axis == 'horizontal':
        image_shifted = np.roll(mask, -center_col, axis=1)
        flipped_image = np.fliplr(image_shifted)
        return np.roll(flipped_image, center_col, axis=1)
    
def compute_overlap(image1, image2):
    """compute the overlap score"""
    
    intersection = np.logical_and(image1, image2)
    union = np.logical_or(image1, image2)
    overlap = np.sum(intersection) / np.sum(union)
    
    return overlap

def symmetry_score(image):
    """compute the vertical and horizontal symmetry scores"""
    mask = load_image(image) # load the image from path
    

    vert_flipped = flip_image_centered(mask, 'vertical')
    horiz_flipped = flip_image_centered(mask, 'horizontal')
    
    vertical_symmetry_score = compute_overlap(mask, vert_flipped)
    horizontal_symmetry_score = compute_overlap(mask, horiz_flipped)
    total_score = round((vertical_symmetry_score + horizontal_symmetry_score) / 2, 4)

    return total_score