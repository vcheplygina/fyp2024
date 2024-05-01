from scipy.stats import skew, kurtosis
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt


def plot_histogram(image_id: str):
    metadata = pd.read_csv("data/metadata.csv")
    d = metadata.query(f"img_id=='{image_id}.png'")["diagnostic"].item()
    image = cv2.imread(f"good_bad_images/{d}/good/images/{image_id}.png")
    mask = cv2.imread(
        f"good_bad_images/{d}/good/masks/{image_id}_mask.png", cv2.IMREAD_GRAYSCALE
    )
    # split the image into its respective channels, then initialize
    # the tuple of channel names along with our figure for plotting
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(f"color histogram for image: {image_id}")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    channel_stats = {}

    # loop over the image channels
    for chan, color in zip(chans, colors):
        # create a histogram for the current channel and plot it
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
        hist = hist.ravel() / hist.sum()  # Normalize the histogram

        # Calculate mean, std, skewness, and kurtosis for each channel.
        mean_val = np.dot(hist, np.arange(256))
        std_val = np.sqrt(np.dot(hist, (np.arange(256) - mean_val) ** 2))
        skew_val = skew(np.array(hist, dtype=np.float64))
        kurt_val = kurtosis(np.array(hist, dtype=np.float64))

        # Find the peak value (dominant intensity)
        peak_val = np.argmax(hist)

        # Store the statistics in the dictionary.
        channel_stats[color] = {
            "mean": mean_val,
            "std_dev": std_val,
            "skewness": skew_val,
            "kurtosis": kurt_val,
            "peak_val": peak_val,
        }
    output_stats = {}
    for stat in ["mean", "std_dev", "skewness", "kurtosis", "peak_val"]:
        output_stats[stat] = (
            channel_stats["r"][stat],
            channel_stats["g"][stat],
            channel_stats["b"][stat],
        )

    return output_stats


img_id = "PAT_26_37_865"

stats = plot_histogram(img_id)
print(stats)
plt.show()
