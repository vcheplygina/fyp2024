"""
FYP project imaging
"""

import os
import sys

from os.path import exists
import pandas as pd
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from template.extract_features_train import *
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
    "patient_id",
    "diagnostic",
]
dtype = [
    ("asymmetry", np.float16),
    ("compactness", np.float16),
    ("blue_white_veil", np.float16),
    ("sd_r", np.float16),
    ("sd_g", np.float16),
    ("sd_b", np.float16),
    ("mean_r", np.float16),
    ("mean_g", np.float16),
    ("mean_b", np.float16),
    ("peak_r", np.float16),
    ("peak_g", np.float16),
    ("peak_b", np.float16),
    ("patient_id", "<U50"),  # String type with max length 50
    ("diagnostic", "<U50"),  # String type with max length 50
]

num_features = len(dtype)
features = np.zeros(num_images, dtype=dtype)

for i, val in enumerate(get_data()):
    img_path = "data/images/" + val["img"]
    mask_path = "data/masks/" + val["mask"]

    # This ensures that we are not using image without a mask
    if exists(img_path) and exists(mask_path):
        x = extract_features_train(image_path=img_path, mask=mask_path)
        if len(x) == len(dtype):
            # Assign each element of x to the corresponding field in features
            for j, field in enumerate(dtype):
                features[i][field[0]] = x[j]
            # Assign patient_id and diagnostic
            features[i]["patient_id"] = x[-2]
            features[i]["diagnostic"] = x[-1]
        else:
            print(f"Skipping image {val['img']} due to mismatch in feature dimensions.")

df = pd.DataFrame(features, columns=[val[0] for val in dtype])
cleaned_df = df.dropna(how="any")

# Once all data is processed, save it to CSV
cleaned_df.to_csv("template/features/features_training.csv", index=False)
