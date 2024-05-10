import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.segmentation import slic, mark_boundaries
from skimage.color import label2rgb
from skimage.measure import regionprops
import cv2
import math
import os

def convert_to_rgb(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image[:, :, :3] if image.shape[-1] == 4 else image

def preprocess_mask(mask):
    grayscale_mask = np.mean(mask, axis=2)
    binary_mask = (grayscale_mask > 0).astype(np.uint8)
    return binary_mask

def manhatten(true_color, pixel_color):
    return np.sum(np.abs(true_color - pixel_color))

def cancer_probability(marked_count, all_segments):
    return round((marked_count / all_segments), 2)

def get_slic_visual(image_path, mask_path):
    if not os.path.exists(image_path) or not os.path.exists(mask_path):
        return "Error: Image or mask file does not exist. Check file paths."

    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path)

    if image is None or mask is None:
        return "Error: Failed to load image or mask. Check file integrity."

    image = convert_to_rgb(image)
    mask = preprocess_mask(mask)
    
    segments_slic = slic(image, n_segments=100, compactness=10, sigma=1, mask=mask)
    not_match = 0
    threshold_for_manhatten = 100
    color_dict = {
            'CANCER1':[(46, 50, 49),0],
            'CANCER2':[(116, 96, 80),0],
            'CANCER3':[(42, 44, 43),0],
            'CANCER4':[(157, 137, 112),0],
            'CANCER5':[(112, 93, 82),0],
            'CANCER6':[(136, 117, 105),0],
            'CANCER7':[(116, 93, 79),0],
            'CANCER8':[(93, 71, 61),0],
            'CANCER9':[(90, 76, 71),0],
            'CANCER10':[(97, 80, 75),0],
            'NONCANCER1':[(198, 138, 109),0],
            'NONCANCER2':[(124, 76, 56),0],
            'NONCANCER3':[(108, 66, 48),0],
            'NONCANCER4':[(124, 78, 60),0],
            'NONCANCER5':[(151, 105, 91),0],
            'NONCANCER6':[(120, 73, 53),0],
            'NONCANCER7':[(97, 70, 58),0],
            'NONCANCER8':[(135, 82, 58),0],
            'NONCANCER9':[(92, 65, 51),0],
            'NONCANCER10':[(136, 82, 60),0]
    }
    
    for segment in np.unique(segments_slic):
        segment_mask = segments_slic == segment
        if np.any(mask[segment_mask]):
            segment_pixels = image[segment_mask]
            mean_color = np.mean(segment_pixels, axis=0)
            closest_match, min_distance = None, float('inf')
            for color_name, (color_value, count) in color_dict.items():
                distance = manhatten(color_value, mean_color)
                if distance < min_distance:
                    min_distance, closest_match = distance, color_name
            if min_distance < threshold_for_manhatten:
                color_dict[closest_match][1] += 1
            else:
                not_match += 1

    cancer_segments_count, non_cancer_segments_count = 0, 0
    for key, (value, count) in color_dict.items():
        if 'CANCER' in key:
            cancer_segments_count += count
        else:
            non_cancer_segments_count += count

    return cancer_probability(cancer_segments_count, cancer_segments_count + non_cancer_segments_count)

