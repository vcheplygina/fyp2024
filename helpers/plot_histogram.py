import cv2
from matplotlib import pyplot as plt
import os


def plot_histogram(img, mask):
    try:
        image = cv2.imread(img)
        mask = cv2.imread(mask, cv2.IMREAD_GRAYSCALE)
        chans = cv2.split(image)
        colors = ("b", "g", "r")

        # Create a single histogram plot
        plt.figure(figsize=(8, 6))

        # Loop over the image channels
        for chan, color in zip(chans, colors):
            # Create a histogram for the current channel and plot it
            hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
            plt.plot(hist, color=color, label=color.upper() + ' channel')

        plt.title('Histogram of All Channels')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')
        plt.legend()
        plt.grid(True)
        plt.show()

    except Exception as e:
        print(f"Error: Plotting histogram failed for img: {img}, mask: {mask}")
