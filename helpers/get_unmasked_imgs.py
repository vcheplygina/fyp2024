import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)

from helpers.get_data import *


def find_images_without_masks(images_dir, masks_dir):
    image_files = os.listdir(images_dir)
    mask_files = os.listdir(masks_dir)

    # Extract the filenames without extension
    image_names = [os.path.splitext(file)[0] for file in image_files]
    mask_names = [os.path.splitext(file)[0] for file in mask_files]

    # Find images without corresponding masks
    images_without_masks = [image for image in image_names if image + "_mask" not in mask_names]

    return images_without_masks


# Example usage:
images_folder = "data/images"
masks_folder = "data/masks"
missing_masks = find_images_without_masks(images_folder, masks_folder)
print("Images without corresponding masks:")
for image in missing_masks:
    print(image)

