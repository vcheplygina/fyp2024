import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.color import rgba2rgb
from collections import Counter

# Define paths to images and masks
imgs_cancer = 'good_bad_images\\CANCER\\images'
masks_cancer = 'good_bad_images\\CANCER\\masks'
imgs_noncancer = 'good_bad_images\\NONCANCER\\images'
masks_noncancer = 'good_bad_images\\NONCANCER\\masks'


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
        segments_slic = slic(image, n_segments=100, compactness=10, sigma=1, start_label=1, mask=mask, max_size_factor=3)
        

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

    
    # Count all colors and select top n
    color_counts = Counter(all_colors)
    top_colors = 10
    most_common_colors = color_counts.most_common(top_colors)

    # Calculate the total number of colors
    total_color_count = sum(color_counts.values())

    # Calculate relative frequency (to sum to 1)
    most_common_colors_relative = [(color, count / total_color_count) for color, count in most_common_colors]

    # Print colors
    for col in most_common_colors_relative:
        print(f"{group_name}: {col[0]}")

    # Plot and saving plot as png
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(most_common_colors_relative)), [count for _, count in most_common_colors_relative],
        color=[f'#{int(color[0]):02x}{int(color[1]):02x}{int(color[2]):02x}' for color, _ in most_common_colors_relative])
    plt.xticks(range(len(most_common_colors_relative)), [f'({color[0]}, {color[1]}, {color[2]})' for color, _ in most_common_colors_relative], rotation=45)
    plt.xlabel('Colors')
    plt.ylabel('Relative Frequency')
    plt.title(f'Top {top_colors} most common colors in {group_name} groups')
    plt.subplots_adjust(bottom=0.2)  
    plt.savefig(f'features\\get_top_colors\\histograms\\{group_name}_NEW_{top_colors}.png', dpi=300, bbox_inches='tight')

    # Optional show each plot
    #plt.show()
    



# Lists, where paths will be appended
paths_list =[]
masks_list=[]

# Append each path
paths_list.append(imgs_cancer)
#paths_list.append(imgs_noncancer)

masks_list.append(masks_cancer)
#masks_list.append(masks_noncancer)


# Iterate through paths, but with step 2
# I want to merge current(good) and next(bad) groups, due to our image separation in different groups
for i in range(0,len(paths_list)):

    #Get group name, based on filename
    parts = paths_list[i].split('\\')  
    group_name = parts[1]  


    # Get image and mask paths
    path_imgs = [os.path.join(paths_list[i], filename) for filename in os.listdir(paths_list[i])]
    path_masks = [os.path.join(masks_list[i], os.path.splitext(filename)[0] + '_mask.png') for filename in os.listdir(paths_list[i])]


    # Load images and masks
    images = [cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB) for img_path in path_imgs]
    masks = [cv2.imread(mask_path, 0) for mask_path in path_masks]  

    try:
        print(f"Working on: {group_name}")

        get_colors(images,masks,group_name)

        print('----------------------')
    except Exception as e:
        print(f"Error processing images: {e}")

print("Done")
