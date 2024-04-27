import cv2

# Read the original image
image = cv2.imread("Raw_images_masks/ACK/good/PAT_104_1754_276.png")

# Read the mask image
mask = cv2.imread(
    "Raw_images_masks/ACK/good/masks/PAT_104_1754_276_mask.png", cv2.IMREAD_GRAYSCALE
)

# Apply the mask to the original image
masked_image = cv2.bitwise_and(image, image, mask=mask)
# Perform segmentation, feature extraction, or other analysis on the masked image
# Example: You can use thresholding for segmentation
ret, thresholded_image = cv2.threshold(masked_image, 127, 255, cv2.THRESH_BINARY)

# Display the original image, mask, and processed image
cv2.imshow("Original Image", image)
cv2.imshow("Mask", mask)
cv2.imshow("Masked Image", masked_image)
cv2.imshow("Thresholded Image", thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
