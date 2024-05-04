import numpy as np
import cv2


def get_histogram_data(img, mask):
    image = cv2.imread(img)
    mask = cv2.imread(mask, cv2.IMREAD_GRAYSCALE)
    # split the image into its respective channels, then initialize
    # the tuple of channel names along with our figure for plotting
    try:
        chans = cv2.split(image)
        colors = ("b", "g", "r")
        channel_stats = {}

        # loop over the image channels
        for chan, color in zip(chans, colors):
            # create a histogram for the current channel and plot it
            hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
            hist = hist.ravel() / hist.sum()  # Normalize the histogram

            # Calculate mean, std, skewness, and kurtosis for each channel.
            mean_val = np.dot(hist, np.arange(256))
            std_val = np.sqrt(np.dot(hist, (np.arange(256) - mean_val) ** 2))

            # Find the peak value (dominant intensity)
            peak_val = np.argmax(hist)

            # Store the statistics in the dictionary.
            channel_stats[color] = {
                "mean": mean_val,
                "std_dev": std_val,
                "peak_val": peak_val,
            }
        return channel_stats
    except Exception as e:
        print(f"err: histogram data, img: {img}")
        return None
