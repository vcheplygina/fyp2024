import cv2
import numpy as np


def compactness(mask_path):
    try:
        """assesses the compactness of the lesion - irregularity of edges"""
        contours, _ = cv2.findContours(
            mask_path, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        largest_contour = max(contours, key=cv2.contourArea)

        area = cv2.contourArea(largest_contour)
        perimeter = cv2.arcLength(largest_contour, True)

        compactness = (4 * np.pi * area) / (perimeter**2)

        return compactness
    except Exception as e:
        print(e)

