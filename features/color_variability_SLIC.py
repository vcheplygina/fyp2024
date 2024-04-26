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






def get_slic_visual(image, mask):
    # Convert image to RGB if it is not already in RGB format
    if image.shape[-1] == 4:
        image = convert_to_rgb(image)

    mask = preprocess_mask(mask)
    # Apply SLIC algorithm
    segments_slic = slic(image, n_segments=100, compactness=10, sigma=1, start_label=1, mask=mask)

    # Visualizing the segments
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax[0].set_title('Original Image')
    ax[0].axis('off')

    ax[1].imshow(mask, cmap='gray')
    ax[1].set_title('Mask')
    ax[1].axis('off')

    marked_image = mark_boundaries(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), segments_slic)
    ax[2].imshow(marked_image)
    ax[2].set_title('Segmented Image')
    ax[2].axis('off')

    plt.show()

   



img = cv2.imread('good_bad_images\MEL\good\images\david\PAT_109_868_723.png')
mask = cv2.imread('good_bad_images\MEL\good\masks\david\PAT_109_868_723_mask.png')



#print(get_slic(img,mask))
print(get_slic_visual(img,mask))





