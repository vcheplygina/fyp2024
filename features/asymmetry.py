import cv2
import numpy as np


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

