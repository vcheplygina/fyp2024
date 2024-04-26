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

def test_images(image_path, mask_path, save_folder):
    '''used to test images to visually assess  the correctness of our algorithm'''
    image, mask = load_image(image_path, mask_path)
    detected_mask = detect_blue_white(image, mask)
    result = coverage_ratio(detected_mask, mask)
    
    # check if the save folder exists, if not, create it
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    
    """display the original, mask, and detected mask images with coverage ratio and saves them in given folder"""
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('Manual Mask')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(detected_mask, cv2.COLOR_GRAY2RGB))
    plt.title(f'Detected Mask')
    plt.axis('off')

    plt.suptitle(f'Coverage Ratio: {result:.2%}')
    plt.show()
    
    # save the figure to the designated save folder
    save_path = os.path.join(save_folder, f"result_{os.path.basename(image_path)}.png")
    plt.savefig(save_path)
    plt.close()
    
