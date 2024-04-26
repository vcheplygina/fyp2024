import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.segmentation import slic, mark_boundaries
from skimage.color import label2rgb
from skimage.measure import regionprops
import cv2
# Helper function to convert RGBA to RGB
def convert_to_rgb(image):
    return image[:, :, :3]  # Drops the alpha channel
def preprocess_mask(mask):
    """
    Preprocess the mask array to make it compatible with the SLIC algorithm.
    """
    # Convert the mask to grayscale
    grayscale_mask = np.mean(mask, axis=2)
    # Threshold the grayscale mask to obtain a binary mask
    binary_mask = (grayscale_mask > 0).astype(np.uint8)
    return binary_mask

# Function to apply SLIC, extract features, and visualize the results
def get_slic(image, mask):
    # Convert image to RGB if it is not already in RGB format
    if image.shape[-1] == 4:
        image = convert_to_rgb(image)

    mask = preprocess_mask(mask)
    # Apply SLIC algorithm
    segments_slic = slic(image, n_segments=5, compactness=5, sigma=1, start_label=1,mask=mask)

    color_dict = {
        'white': [(175, 172, 167), 0],
        'light-brown': [(143, 100, 76), 0],
        'dark-brown': [(82, 70, 67), 0],
        'blue-grey': [(59, 63, 75), 0],
        'red': [(146, 80, 86), 0],
        'black': [(48, 51, 49), 0]
    }
    def manhatten(true_color, pixel_color):
        return np.sum(np.abs(true_color - pixel_color))

    for i in np.unique(slic):
        if np.sum(mask[slic == i]) == 0:
            continue
        norm = np.mean(image[slic == i], axis=0)
        rgb = np.array((norm * 255).astype(int))

        min_dist = 1000
        color = None
        for key, value in color_dict.items():
            dist = manhatten(rgb, value[0])
            if dist < min_dist:
                min_dist = dist
                color = key

        color_dict[color][1] += 1

    return [v[1] for v in color_dict.values()]

img = cv2.imread('good_bad_images\MEL\good\images\david\PAT_109_868_723.png')
mask = cv2.imread('good_bad_images\MEL\good\masks\david\PAT_109_868_723_mask.png')
print(get_slic(img,mask))





