import numpy as np
import cv2
import os
import json


def calculate_histograms(img_ids: list[str], group: str):
    histograms = {}  # Dictionary to store histograms per image

    for id in img_ids:
        image = cv2.imread(f"Raw_images_masks/${group}/good/${id}.png")

        # Read the mask image
        mask = cv2.imread(
            f"Raw_images_masks/${group}/good/${id}_mask.png",
            cv2.IMREAD_GRAYSCALE,
        )

        # Apply the mask to the original image
        masked_image = cv2.bitwise_and(image, image, mask=mask)
        # Perform segmentation, feature extraction, or other analysis on the masked image
        # Example: You can use thresholding for segmentation
        ret, thresholded_image = cv2.threshold(
            masked_image, 127, 255, cv2.THRESH_BINARY
        )

        if masked_image is None:
            print(f"Error: Unable to read image '{filename}'")
            continue

        # Convert image from BGR to RGB
        image_rgb = cv2.cvtColor(masked_image, cv2.COLOR_BGR2RGB)

        # Calculate histograms for each color channel
        histogram_r = cv2.calcHist([image_rgb], [0], None, [256], [0, 256])
        histogram_g = cv2.calcHist([image_rgb], [1], None, [256], [0, 256])
        histogram_b = cv2.calcHist([image_rgb], [2], None, [256], [0, 256])

        # Store histograms in a dictionary
        histograms[os.path.basename(filename)] = {
            "histogram_r": histogram_r.flatten().tolist(),
            "histogram_g": histogram_g.flatten().tolist(),
            "histogram_b": histogram_b.flatten().tolist(),
        }

    return histograms


def calculate_color_composition(histogram_data):
    color_composition = {}
    for filename, hist_data in histogram_data.items():
        total_pixels = (
            sum(hist_data["histogram_r"])
            + sum(hist_data["histogram_g"])
            + sum(hist_data["histogram_b"])
        )
        red_proportion = sum(hist_data["histogram_r"]) / total_pixels
        green_proportion = sum(hist_data["histogram_g"]) / total_pixels
        blue_proportion = sum(hist_data["histogram_b"]) / total_pixels
        color_composition[filename] = {
            "red_proportion": red_proportion,
            "green_proportion": green_proportion,
            "blue_proportion": blue_proportion,
        }
    return color_composition


# Function to calculate color distribution from histograms
def calculate_color_distribution(histogram_data):
    color_distribution = {}
    for filename, hist_data in histogram_data.items():
        # Convert histograms to NumPy arrays for easier calculation
        histogram_r = np.array(hist_data["histogram_r"])
        histogram_g = np.array(hist_data["histogram_g"])
        histogram_b = np.array(hist_data["histogram_b"])

        # Calculate statistical measures for each color channel
        mean_r = np.mean(histogram_r)
        mean_g = np.mean(histogram_g)
        mean_b = np.mean(histogram_b)

        variance_r = np.var(histogram_r)
        variance_g = np.var(histogram_g)
        variance_b = np.var(histogram_b)

        skewness_r = np.mean(((histogram_r - mean_r) / np.sqrt(variance_r)) ** 3)
        skewness_g = np.mean(((histogram_g - mean_g) / np.sqrt(variance_g)) ** 3)
        skewness_b = np.mean(((histogram_b - mean_b) / np.sqrt(variance_b)) ** 3)

        kurtosis_r = np.mean(((histogram_r - mean_r) / np.sqrt(variance_r)) ** 4) - 3
        kurtosis_g = np.mean(((histogram_g - mean_g) / np.sqrt(variance_g)) ** 4) - 3
        kurtosis_b = np.mean(((histogram_b - mean_b) / np.sqrt(variance_b)) ** 4) - 3

        color_distribution[filename] = {
            "mean_r": mean_r,
            "mean_g": mean_g,
            "mean_b": mean_b,
            "variance_r": variance_r,
            "variance_g": variance_g,
            "variance_b": variance_b,
            "skewness_r": skewness_r,
            "skewness_g": skewness_g,
            "skewness_b": skewness_b,
            "kurtosis_r": kurtosis_r,
            "kurtosis_g": kurtosis_g,
            "kurtosis_b": kurtosis_b,
        }
    return color_distribution


def find_intensity_peaks(histogram_data, threshold=0.1):
    intensity_peaks = {}
    for filename, hist_data in histogram_data.items():
        # Convert histograms to NumPy arrays for easier calculation
        histogram_r = np.array(hist_data["histogram_r"])
        histogram_g = np.array(hist_data["histogram_g"])
        histogram_b = np.array(hist_data["histogram_b"])

        # Find peaks above threshold
        peaks_r = np.where(histogram_r > threshold * np.max(histogram_r))[0]
        peaks_g = np.where(histogram_g > threshold * np.max(histogram_g))[0]
        peaks_b = np.where(histogram_b > threshold * np.max(histogram_b))[0]

        intensity_peaks[filename] = {
            "peaks_r": peaks_r.tolist(),
            "peaks_g": peaks_g.tolist(),
            "peaks_b": peaks_b.tolist(),
        }
    return intensity_peaks


def calculate_color_homogeneity(histogram_data):
    color_homogeneity = {}
    for filename, hist_data in histogram_data.items():
        # Convert histograms to NumPy arrays for easier calculation
        histogram_r = np.array(hist_data["histogram_r"])
        histogram_g = np.array(hist_data["histogram_g"])
        histogram_b = np.array(hist_data["histogram_b"])

        # Calculate variance of color values within each channel
        variance_r = np.var(histogram_r)
        variance_g = np.var(histogram_g)
        variance_b = np.var(histogram_b)

        # Compute overall color homogeneity by averaging variances across channels
        overall_homogeneity = (variance_r + variance_g + variance_b) / 3

        color_homogeneity[filename] = overall_homogeneity

    return color_homogeneity


# Function to save histograms to a JSON file
def save_histograms_to_json(histograms, filename):
    with open(filename, "w") as f:
        json.dump(histograms, f)


# Function to load histograms from a JSON file
def load_histograms_from_json(filename):
    with open(filename, "r") as f:
        histograms = json.load(f)
    return histograms


# List of image filenames
image_filenames = ["toy.png", "zlodej.jpg"]

# Calculate histograms
histograms = calculate_histograms(image_filenames)

# Save histograms to a JSON file
save_histograms_to_json(histograms, "histograms.json")

# Load histograms from the JSON file
loaded_histograms = load_histograms_from_json("histograms.json")

color_composition = calculate_color_composition(loaded_histograms)
color_distribution = calculate_color_distribution(loaded_histograms)
intensity_peaks = find_intensity_peaks(loaded_histograms)
color_homogeneity = calculate_color_homogeneity(loaded_histograms)

print(color_distribution)
print(color_homogeneity)
