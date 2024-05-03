"""
FYP project imaging
"""

from os.path import exists
import pandas as pd
import numpy as np
from helpers.get_data import get_data
from features import (
    histogram_data,
    asymmetry,
    blue_white_veil,
    compactness,
    atypical_network,
)

# -------------------
# Main script
# -------------------

# Where we will store the features
file_features = "features/features.csv"
# Where all our images and masks are being stored
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

feature_names = [
    "asymmetry",
    "compactness",
    # "slic_cancer_true",
    # "slic_cancer_false",
    "rgb_mean_value",
    "rgb_standard_deviation",
    "rgb_skewness",
    "rgb_kurtosis",
    "rgb_peak_val",
    "blue_white_veil",
    # "network_structures",
]

num_features = len(feature_names)
features = np.empty(
    num_images, dtype=[(name, "object") for name in feature_names]
)  # Using 'object' type for generic data

for i, val in enumerate(get_data()):
    img_path = "data/images/" + val["img"]
    mask_path = "data/masks/" + val["mask"]

    # This ensures that we are not using image without a mask
    if exists(img_path) and exists(mask_path):
        hist_data = histogram_data.get_histogram_data(img_path, mask_path)
        if hist_data:
            # Convert tuple to a string for CSV storage
            features[i]["rgb_mean_value"] = str(hist_data["mean"])
            features[i]["rgb_skewness"] = str(hist_data["skewness"])
            features[i]["rgb_standard_deviation"] = str(hist_data["std_dev"])
            features[i]["rgb_kurtosis"] = str(hist_data["kurtosis"])
            features[i]["rgb_peak_val"] = str(hist_data["peak_val"])
        asymmetry_data = asymmetry.asymmetry(mask_path)
        if asymmetry_data:
            features[i]["asymmetry"] = asymmetry_data
        bvw_data = blue_white_veil.blue_white_veil(img_path, mask_path)
        if bvw_data:
            features[i]["blue_white_veil"] = bvw_data
        compactness_data = compactness.compactness(mask_path)
        if compactness_data:
            features[i]["compactness"] = compactness_data


# Once all data is processed, save it to CSV
pd.DataFrame(features, columns=feature_names).to_csv(file_features, index=False)
