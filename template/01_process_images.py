"""
FYP project imaging
"""

import os
import sys

from os.path import exists
import pandas as pd
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from template.extract_features import *
from helpers.get_data import get_data

# -------------------
# Main script
# -------------------

# Where we will store the features
metadata_path = "data/metadata.csv"
# Where all our images and masks are being stored
data = get_data()


# Read meta-data into a Pandas dataframe
df = pd.read_csv(metadata_path)

num_images = len(data)


# Set features for extraction to features.csv
feature_names = [
    "asymmetry",
    "compactness",
    "blue_white_veil",
    "sd_r",
    "sd_g",
    "sd_b",
    "mean_r",
    "mean_g",
    "mean_b",
    "peak_r",
    "peak_g",
    "peak_b",
]

num_features = len(feature_names)
features = np.zeros([num_images, num_features], dtype=np.float16)

for i, val in enumerate(get_data()):
    img_path = "data/images/" + val["img"]
    mask_path = "data/masks/" + val["mask"]

    # This ensures that we are not using image without a mask
    if exists(img_path) and exists(mask_path):
        x = extract_features(image=img_path, mask=mask_path)
        features[i, :] = x

df = pd.DataFrame(features)
cleaned_df = df.dropna(how="any")

# Once all data is processed, save it to CSV
cleaned_df.to_csv("template_for_exam/features/features_n.csv", index=False)
