"""
FYP project imaging
"""

import os
from os.path import exists
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from get_data import *

# -------------------
# Main script
# -------------------

# Where we will store the features
file_features = "features/features.csv"

data = get_data()


# Read meta-data into a Pandas dataframe
df = pd.read_csv("data/metadata.csv")

# Extract image IDs and labels from the data.
image_id = list(df["img_id"])
label = np.array(df["diagnostic"])

# Here you could decide to filter the data in some way (see task 0)
# For example you can have a file selected_images.csv which stores the IDs of the files you need
is_nevus = label == "NEV"

num_images = len(image_id)


# Make array to store features
feature_names = [
    "asymmetry",
    "color variability",
    "blue white veil",
    "compactness",
    "atypical network",
]
num_features = len(feature_names)
features = np.zeros([num_images, num_features], dtype=np.float16)

# for i, val in enumerate(get_data()):
# img_path = "./data/images/" + val["img"]
# mask_path = "./data/masks/" + val["mask"]

# if exists(img_path) and exists(mask_path):
# print("Hello World")
# pass


# # Loop through all images (now just 10 for demonstration)
# for i in np.arange(10):

# # Define filenames related to this image
# file_image = path_image + os.sep + image_id[i]

# if exists(file_image):

# # Read the image
# im = plt.imread(file_image)
# im = np.float16(im)

# # Measure features - this does not do anything useful yet!
# x = extract_features(im)

# # Store in the variable we created before
# features[i, :] = x


# # Save the image_id used + features to a file
# df_features = pd.DataFrame(features, columns=feature_names)
# df_features.to_csv(file_features, index=False)
