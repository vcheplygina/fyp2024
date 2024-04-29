###
# This file will print top n colors
###

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.color import rgba2rgb
from collections import Counter


def convert_to_rgb(image):
    '''
    Convert from RGBA to RGB
    '''
    return rgba2rgb(image) if image.shape[-1] == 4 else image

def preprocess_mask(mask):
    '''
    Convert to binary image
    '''
    return mask > 0 if mask.ndim > 2 else mask

def get_colors(images, masks, group_name):
    '''
    Input: list of images,masks and group name
    Output: No output but creating PNGs with histograms
    '''
    slic_filename_counter = 1
    # Unzip list of images and masks
    for image, mask in zip(images, masks):
        # If image in RGBA (4dimenstions), use function convert_to_rgb
        if image.shape[-1] == 4:
            image = convert_to_rgb(image)
        # Convert mask using function
        mask = preprocess_mask(mask)

        # Perform SLIC ags. that will divide lession (based on mask) into n_segments based on neighbors colors
        segments_slic = slic(image, n_segments=100, compactness=10, sigma=1, start_label=1, mask=mask)
        

        # Optional saving slic figs
        '''
        fig, ax = plt.subplots(1, figsize=(10, 6))
        ax.imshow(mark_boundaries(image, segments_slic))
        ax.set_axis_off()
        plt.tight_layout()
        plt.savefig(f'features\\get_top_colors\\100segments\\slic\\{group_name}_{slic_filename_counter}.png', dpi=300, bbox_inches='tight')
        slic_filename_counter += 1
        '''

        # Iterate through each segment and save pixel colors
        all_colors = []
        for segment_label in np.unique(segments_slic):
            segment_mask = segments_slic == segment_label
            segment_color = np.mean(image[segment_mask], axis=0)
            all_colors.append(tuple(segment_color.astype(int)))

    # Count all colors and select top 10
    color_counts = Counter(all_colors)
    most_common_colors = color_counts.most_common(2)

    # Calculate the total number of colors
    total_color_count = sum(color_counts.values())

    # Calculate relative frequency (to sum to 1)
    most_common_colors_relative = [(color, count / total_color_count) for color, count in most_common_colors]

    # Print 2 colors
    print(most_common_colors_relative)

    # Plot and saving plot as png
    '''
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(most_common_colors_relative)), [count for _, count in most_common_colors_relative],
        color=[f'#{int(color[0]):02x}{int(color[1]):02x}{int(color[2]):02x}' for color, _ in most_common_colors_relative])
    plt.xticks(range(len(most_common_colors_relative)), [f'({color[0]}, {color[1]}, {color[2]})' for color, _ in most_common_colors_relative], rotation=45)
    plt.xlabel('Colors')
    plt.ylabel('Relative Frequency')
    plt.title(f'Top 10 most common colors in {group_name}')
    plt.subplots_adjust(bottom=0.2)  
    plt.savefig(f'features\\get_top_colors\\100segments\\{group_name}_top10_100segments.png', dpi=300, bbox_inches='tight')

    # Optional show each plot
    #plt.show()
    
    '''


# Define paths to images and masks
# This is due debugging issues and clearness
ACK_good_imgs_path = 'good_bad_images\\ACK\\good\\images'
ACK_good_masks_path = 'good_bad_images\\ACK\\good\\masks'
ACK_bad_imgs_path = 'good_bad_images\\ACK\\bad\\images'
ACK_bad_masks_path = 'good_bad_images\\ACK\\bad\\masks'

BCC_good_imgs_path = 'good_bad_images\\BCC\\good\\images'
BCC_good_masks_path = 'good_bad_images\\BCC\\good\\masks'
BCC_bad_imgs_path = 'good_bad_images\\BCC\\bad\\images'
BCC_bad_masks_path = 'good_bad_images\\BCC\\bad\\masks'

MEL_good_imgs_path = 'good_bad_images\\MEL\\good\\images\\lucie'
MEL_good_masks_path = 'good_bad_images\\MEL\\good\\masks\\lucie'
MEL_bad_imgs_path = 'good_bad_images\\MEL\\bad\\images\\lucie'
MEL_bad_masks_path = 'good_bad_images\\MEL\\bad\\masks\\lucie'

NEV_good_imgs_path = 'good_bad_images\\NEV\\good\\images'
NEV_good_masks_path = 'good_bad_images\\NEV\\good\\masks'
NEV_bad_imgs_path = 'good_bad_images\\NEV\\bad\\images'
NEV_bad_masks_path = 'good_bad_images\\NEV\\bad\\masks'

SCC_good_imgs_path = 'good_bad_images\\SCC\\good\\images\\matus'
SCC_good_masks_path = 'good_bad_images\\SCC\\good\\masks\\matus'
SCC_bad_imgs_path = 'good_bad_images\\SCC\\bad\\images\\matus'
SCC_bad_masks_path = 'good_bad_images\\SCC\\bad\\masks\\matus'

SEK_good_imgs_path = 'good_bad_images\\SEK\\good\\images'
SEK_good_masks_path = 'good_bad_images\\SEK\\good\\masks'
SEK_bad_imgs_path = 'good_bad_images\\SEK\\bad\\images'
SEK_bad_masks_path = 'good_bad_images\\SEK\\bad\\masks'

# Lists, where paths will be appended
paths_list =[]
masks_list=[]

# Append each path
paths_list.append(ACK_good_imgs_path)
paths_list.append(ACK_bad_imgs_path)
paths_list.append(BCC_good_imgs_path)
paths_list.append(BCC_bad_imgs_path)
paths_list.append(MEL_good_imgs_path)
paths_list.append(MEL_bad_imgs_path)
paths_list.append(NEV_good_imgs_path)
paths_list.append(NEV_bad_imgs_path)
paths_list.append(SCC_good_imgs_path)
paths_list.append(SCC_bad_imgs_path)
paths_list.append(SEK_good_imgs_path)
paths_list.append(SEK_bad_imgs_path)

masks_list.append(ACK_good_masks_path)
masks_list.append(ACK_bad_masks_path)
masks_list.append(BCC_good_masks_path)
masks_list.append(BCC_bad_masks_path)
masks_list.append(MEL_good_masks_path)
masks_list.append(MEL_bad_masks_path)
masks_list.append(NEV_good_masks_path)
masks_list.append(NEV_bad_masks_path)
masks_list.append(SCC_good_masks_path)
masks_list.append(SCC_bad_masks_path)
masks_list.append(SEK_good_masks_path)
masks_list.append(SEK_bad_masks_path)


# Iterate through paths, but with step 2
# I want to merge current(good) and next(bad) groups, due to our image separation in different groups
for i in range(0,len(paths_list),2):

    #Get group name, based on filename
    parts = paths_list[i].split('\\')  
    group_name = parts[1]  


    # Get image and mask paths
    path_imgs_good = [os.path.join(paths_list[i], filename) for filename in os.listdir(paths_list[i])]
    path_masks_good = [os.path.join(masks_list[i], os.path.splitext(filename)[0] + '_mask.png') for filename in os.listdir(paths_list[i])]
    path_imgs_bad = [os.path.join(paths_list[i+1], filename) for filename in os.listdir(paths_list[i+1])]
    path_masks_bad = [os.path.join(masks_list[i+1], os.path.splitext(filename)[0] + '_mask.png') for filename in os.listdir(paths_list[i+1])]

    # Join good and bad images paths
    path_imgs_combined = path_imgs_good + path_imgs_bad
    path_masks_combined = path_masks_good + path_masks_bad

    # Load images and masks
    images = [cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB) for img_path in path_imgs_combined]
    masks = [cv2.imread(mask_path, 0) for mask_path in path_masks_combined]  

    try:
        print(f"Working on: {group_name}")

        get_colors(images,masks,group_name)

        print('----------------------')
    except Exception as e:
        print(f"Error processing images: {e}")

print("Done")




#### Output of 2 most used colors

# ACK: (115, 107, 112), (139, 109, 100)
# BCC: (153, 136, 130), (159, 149, 150)
# MEL: (186, 151, 138), (148, 104, 88)
# NEV: (173, 173, 171), (179, 167, 167)
# SCC: (156, 109, 121), (153, 101, 111)
# SEK: (173, 140, 113), (195, 170, 141)