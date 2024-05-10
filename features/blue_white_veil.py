import cv2
import numpy as np


def get_blue_white_veil(image_path: str, mask_path: str):
    """calculate the coverage ratio of blue-white veil areas"""
    # 1) load the image and its mask
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    try:
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
    except Exception as e:
        print(f"err: blue white veil, image: {image_path}")
