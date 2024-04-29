import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.segmentation import slic, mark_boundaries
from skimage.color import label2rgb
from skimage.measure import regionprops
import cv2

# CHECKLIST
# Re-calibrate colors: Waiting for David to re-do masks



### Can be changed:
# threshold_for_manhatten = 50. Diviation from defined color
# n_segments=100. how many segments will be created from lession



Cancer_groups = ['BCC', 'SCC', 'MEL']
NonCancer_groups = ['SEK', 'ACK', 'NEV']

def convert_to_rgb(image):
    '''
    Function to convert RGBA to RGB (4channels to 3 channels)
    '''
    return image[:, :, :3]

def preprocess_mask(mask):
    """
    Function to convert mask from RGB to Binary
    """
    #Convert the mask to grayscale
    grayscale_mask = np.mean(mask, axis=2) 
    # Threshold the grayscale mask to obtain a binary mask
    binary_mask = (grayscale_mask > 0).astype(np.uint8)
    return binary_mask

def manhatten(true_color, pixel_color):
        '''
        Function to calculate distance between color in color_dict and average color from current segment.
        Example: 'black':[(48, 51, 49),0]  vs [50,55,50], the distance is = 2+4+1= 7
        '''
        return np.sum(np.abs(true_color - pixel_color))

def get_slic_visual(image, mask):
    '''
    This function will use slic alg. to segment the image where is masked. Then It will calculate
    average color in each segment - superpixel. 
    It will compare it to the colors in dictionary, that are pre-defined from all images and add count if match.

    Input: Image and mask
    Output: Group with the most color matches
    '''

    # Set threshold for manhatten function. Default 100
    threshold_for_manhatten = 50

    # Check if image is in RGBA. If true, convert it to RGB
    if image.shape[-1] == 4:
        image = convert_to_rgb(image)

    # Check if mask in binary
    mask = preprocess_mask(mask)

    # Apply SLIC algorithm
    segments_slic = slic(image, n_segments=100, compactness=30, sigma=1, start_label=1, mask=mask)

    # Dictionary with pre-defined colors (top1 from each group or top2)
    color_dict = {
            'ACK1':[(115, 107, 112),0],
            'ACK2':[(139, 109, 100),0],

            'BCC1':[(153, 136, 130),0],
            'BCC2':[(159, 149, 150),0],

            'MEL1':[(186, 151, 138),0],
            'MEL2':[(148, 104, 88),0],

            'NEV1':[(173, 173, 171),0],
            'NEV2':[(179, 167, 167),0],

            'SCC1':[(156, 109, 121),0],
            'SCC2':[(153, 101, 111),0],

            'SEK1':[(173, 140, 113),0],
            'SEK2':[(195, 170, 141),0] 
    }

    # Iterate through unique segments identified by the SLIC algorithm
    for segment in np.unique(segments_slic):
        # If segment in non mask area (pixel in mask = 0), then dont do calculations
        if np.sum(mask[segments_slic == segment]) == 0:
            continue

        # Calculate the mean color of the current segment and convert to RGB
        segment_pixels = image[segments_slic == segment]
        mean_color = np.mean(segment_pixels, axis=0)


        # Compare mean color with pre-defined colors
        for color_name, (color_value, count) in color_dict.items():
            #print(f"Now comparing color_value:{color_value} with mean_color{mean_color}")
            #print(f"manhatten distance is: {manhatten(color_value, mean_color)}")
            if manhatten(color_value, mean_color) < threshold_for_manhatten:
                color_dict[color_name][1] += 1

    # Print results
    for color_name, (color_value, count) in color_dict.items():
        print(f"Segments close to {color_name}: {count}")


    
    # Visualizing the segments - OPTIONAL
    '''
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
    '''

    # Get the key with the most color matches
    max_key = max(color_dict, key=lambda k: color_dict[k][1])

    # Separate group name. SCC1 to SCC...
    max_key_group = max_key[:-1]

    # Return if in cancer group or not in cancer group
    if max_key_group in Cancer_groups:
        return 'Cancer'
    else:
        return 'Non-Cancer'
    

# Read image examples
img = cv2.imread('good_bad_images\ACK\good\images\PAT_26_37_865.png')
mask = cv2.imread('good_bad_images\ACK\good\masks\PAT_26_37_865_mask.png')

print(get_slic_visual(img,mask))




    
