





### Checklist
# SCC: Viacej masiek vo folderi ako obrazkov --> Fix 



import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.color import rgba2rgb
from collections import Counter

def convert_to_rgb(image):
    return rgba2rgb(image) if image.shape[-1] == 4 else image

def preprocess_mask(mask):
    return mask > 0 if mask.ndim > 2 else mask

def get_slic_visual2(images, masks, group_name):
    all_colors = []
    for image, mask in zip(images, masks):
        if image.shape[-1] == 4:
            image = convert_to_rgb(image)
        mask = preprocess_mask(mask)

        segments_slic = slic(image, n_segments=100, compactness=10, sigma=1, start_label=1, mask=mask)

        for segment_label in np.unique(segments_slic):
            segment_mask = segments_slic == segment_label
            segment_color = np.mean(image[segment_mask], axis=0)
            all_colors.append(tuple(segment_color.astype(int)))

    color_counts = Counter(all_colors)
    most_common_colors = color_counts.most_common(10)  # Top 10 most common colors

    # Plot
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(most_common_colors)), [count for _, count in most_common_colors],
            color=[f'#{int(color[0]):02x}{int(color[1]):02x}{int(color[2]):02x}' for color, _ in most_common_colors])
    plt.xticks(range(len(most_common_colors)), [f'({color[0]}, {color[1]}, {color[2]})' for color, _ in most_common_colors], rotation=45)
    plt.xlabel('Colors')
    plt.ylabel('Frequency')
    plt.title(f'Top 10 most common colors in {group_name}')
    plt.subplots_adjust(bottom=0.2)  # Adjust bottom margin
    plt.savefig(f'features\\get_top_colors\\{group_name}.png', dpi=300, bbox_inches='tight')

    plt.show()




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

#SCC_good_imgs_path = 'good_bad_images\\SCC\\good\\images\\matus'
#SCC_good_masks_path = 'good_bad_images\\SCC\\good\\masks\\matus'
#SCC_bad_imgs_path = 'good_bad_images\\SCC\\bad\\images\\matus'
#SCC_bad_masks_path = 'good_bad_images\\SCC\\bad\\masks\\matus'

SEK_good_imgs_path = 'good_bad_images\\SEK\\good\\images'
SEK_good_masks_path = 'good_bad_images\\SEK\\good\\masks'
SEK_bad_imgs_path = 'good_bad_images\\SEK\\bad\\images'
SEK_bad_masks_path = 'good_bad_images\\SEK\\bad\\masks'

paths_list =[]
masks_list=[]

paths_list.append(ACK_good_imgs_path)
paths_list.append(ACK_bad_imgs_path)
paths_list.append(BCC_good_imgs_path)
paths_list.append(BCC_bad_imgs_path)
paths_list.append(MEL_good_imgs_path)
paths_list.append(MEL_bad_imgs_path)
paths_list.append(NEV_good_imgs_path)
paths_list.append(NEV_bad_imgs_path)
#paths_list.append(SCC_good_imgs_path)
#paths_list.append(SCC_bad_imgs_path)
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
#masks_list.append(SCC_good_masks_path)
#masks_list.append(SCC_bad_masks_path)
masks_list.append(SEK_good_masks_path)
masks_list.append(SEK_bad_masks_path)


#paths_list = ['good_bad_images\\ACK\\good\\images','good_bad_images\\ACK\\bad\\images']
#masks_list = ['good_bad_images\\ACK\\good\\masks','good_bad_images\\ACK\\bad\\masks']

print(masks_list)


for i in range(len(paths_list)):

    parts = paths_list[i].split('\\')  
    group_name = parts[1] + '_' + parts[2]  # Concatenate 'ACK' and 'good' with an underscore

    # Get image and mask paths
    path_imgs = [os.path.join(paths_list[i], filename) for filename in os.listdir(paths_list[i])]
    path_masks = [os.path.join(masks_list[i], os.path.splitext(filename)[0] + '_mask.png') for filename in os.listdir(paths_list[i])]



    # Load images and masks
    images = [cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB) for img_path in path_imgs]
    masks = [cv2.imread(mask_path, 0) for mask_path in path_masks]  # Assuming masks are grayscale

    

   
# Process images and masks
    try:
        get_slic_visual2(images, masks, group_name)
    except Exception as e:
        print(f"Error processing images: {e}")
