#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:53:20 2023

@author: vech
"""
import numpy as np
import matplotlib.pyplot as plt

# Import packages for image processing
from skimage import morphology  # for measuring things in the masks
import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------
# Help functions
# ------------------


# Main function to extract features from an image, that calls other functions
def extract_features(image_path, mask_path):

    asymmetry = asymmetry(mask_path)
    color_variability = color_variability()
    blue_white_veil = blue_white_veil(image_path, mask_path)
    compactness = compactness(mask_path)
    atypical_network = atypical_network(image_path, mask_path)

    return np.array([r, g, b], dtype=np.float16)


def asymmetry(mask_path):
    """compute the vertical and horizontal symmetry scores"""
    # 1) load the mask image
    image = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    _, mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # 2) find the center of the lesion
    white_pixels = np.argwhere(mask > 0)
    center_row = np.mean(white_pixels[:, 0]).astype(int)
    center_col = np.mean(white_pixels[:, 1]).astype(int)

    # 3) flip the image along the vertical & horizontal center axes
    # vertical flip
    image_shifted = np.roll(mask, -center_row, axis=0)
    flipped_image = np.flipud(image_shifted)
    vert_flipped = np.roll(flipped_image, center_row, axis=0)
    # horizontal flip
    image_shifted = np.roll(mask, -center_col, axis=1)
    flipped_image = np.fliplr(image_shifted)
    horiz_flipped = np.roll(flipped_image, center_col, axis=1)

    # 4) compute the overlap of the 2 flips:
    # vertical flip
    intersection = np.logical_and(mask, vert_flipped)
    union = np.logical_or(mask, vert_flipped)
    vertical_symmetry_score = np.sum(intersection) / np.sum(union)
    # horizontal flip
    intersection = np.logical_and(mask, horiz_flipped)
    union = np.logical_or(mask, horiz_flipped)
    horizontal_symmetry_score = np.sum(intersection) / np.sum(union)

    # 5) compute the combined symmetry score)
    total_score = round((vertical_symmetry_score + horizontal_symmetry_score) / 2, 4)

    return total_score


def color_variability():
    pass  # to be added


def blue_white_veil(image_path, mask_path):
    """calculate the coverage ratio of blue-white veil areas"""
    # 1) load the image and its mask
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # 2) detect blue-white veil areas in the image using the mask
    cropped_image = cv2.bitwise_and(
        image, image, mask=mask
    )  # crop the image using the mask so that we only work with the lesion
    hsv = cv2.cvtColor(
        cropped_image, cv2.COLOR_BGR2HSV
    )  # convert the cropped image to HSV
    lower_blue = np.array([90, 20, 80])  # define bounds for color detection
    upper_blue = np.array([150, 150, 150])  # HUE | SATURATION | VALUE (brightness)

    # creates a new mask where all pixels fall within the defined bounds
    detected_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 3) calculate the coverage ratio
    veil_area = np.sum(detected_mask > 0)  # total area of the blue-white veil
    total_area = np.sum(mask > 0)
    coverage_ratio = round(veil_area / total_area, 4)

    result = 1 if coverage_ratio > 0 else 0  # if blue-white veil detected, return 1
    return result


def compactness(mask_path):
    """assesses the compactness of the lesion - irregularity of edges"""
    contours, _ = cv2.findContours(
        mask_path, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    largest_contour = max(contours, key=cv2.contourArea)

    area = cv2.contourArea(largest_contour)
    perimeter = cv2.arcLength(largest_contour, True)

    compactness = (4 * np.pi * area) / (perimeter**2)

    return compactness


def atypical_network(image_path, mask_path):
    """detect atypical network"""
    # load the lesion image
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, 0)
    # prepare the lesion image
    cropped_image = cv2.bitwise_and(
        image, image, mask=mask
    )  # crop the image using the mask
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    eq = cv2.equalizeHist(gray)

    edges = cv2.Canny(eq, 100, 200)  # detect edges to find network
    kernel = np.ones((3, 3), np.uint8)  # dilate edges to make the network more visible
    network = cv2.dilate(edges, kernel, iterations=1)

    return network  # return the network mask
