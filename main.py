"""
FYP project imaging
"""

from os.path import exists
import pandas as pd
import numpy as np
from helpers.get_data import get_data
from features.extract_features import (
    asymmetry,
    blue_white_veil,
    compactness,
    atypical_network,
)
from features import (
    histogram_data,
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

num_images = len(data)

# TODO: is slic done?
feature_names = [
    "img_id",
    "asymmetry",
    "compactness",
    # "slic_cancer_true",
    # "slic_cancer_false",
    "mean_r",
    "mean_g",
    "mean_b",
    "sd_r",
    "sd_g",
    "sd_b",
    "peak_r",
    "peak_g",
    "peak_b",
    "blue_white_veil",
    "network_structures",
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
        asymmetry_data = asymmetry(mask_path)
        bvw_data = blue_white_veil(img_path, mask_path)
        compactness_data = compactness(mask_path)
        features[i]["img_id"] = val["img"].split(".")[0]
        network_data = atypical_network(img_path, mask_path)

        if hist_data is not None:
            features[i]["mean_r"] = hist_data["r"]["mean"]
            features[i]["mean_g"] = hist_data["g"]["mean"]
            features[i]["mean_b"] = hist_data["b"]["mean"]
            features[i]["sd_r"] = hist_data["r"]["std_dev"]
            features[i]["sd_g"] = hist_data["g"]["std_dev"]
            features[i]["sd_b"] = hist_data["b"]["std_dev"]
            features[i]["peak_r"] = hist_data["r"]["peak_val"]
            features[i]["peak_g"] = hist_data["g"]["peak_val"]
            features[i]["peak_b"] = hist_data["b"]["peak_val"]
        if asymmetry_data is not None:
            features[i]["asymmetry"] = asymmetry_data
        if bvw_data is not None:
            features[i]["blue_white_veil"] = bvw_data
        if compactness_data is not None:
            features[i]["compactness"] = compactness_data
        if network_data is not None:
            features[i]["network_structures"] = network_data


# Once all data is processed, save it to CSV
pd.DataFrame(features, columns=feature_names).to_csv(file_features, index=False)
