from skimage.segmentation import slic, mark_boundaries
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize


# Function to get us some example images and their masks, and resize them
def prepare_im(im_id):

    path = "Raw_images_masks/ACK/good/"

    im = plt.imread(path + im_id + ".png")
    im = resize(im, (im.shape[0] // 4, im.shape[1] // 4), anti_aliasing=True)

    # gt = plt.imread(path + "masks/" + im_id + "_mask.png")
    # gt = resize(
    # gt, (gt.shape[0] // 4, gt.shape[1] // 4), anti_aliasing=False
    # )  # Setting it to True creates values that are not 0 or 1

    return im


# Get some examples

im1 = prepare_im("toy")
example_im = im1


# plt.imshow(mask1, cmap="gray")
segments_slic = slic(example_im, n_segments=4, compactness=1, sigma=3, start_label=1)


# Show the results
fig, ax = plt.subplots(1, 2, figsize=(10, 10), sharex=True, sharey=True)

ax[0].imshow(example_im)
ax[0].set_title("Original")

ax[1].imshow(mark_boundaries(example_im, segments_slic))
ax[1].set_title("SLIC")

plt.tight_layout()
plt.show()
