import cv2
import numpy as np

# test

# Read the original image
original_image = cv2.imread('add_image_filepath')

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and help with edge detection
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply Canny edge detector
edges = cv2.Canny(blurred_image, 50, 150)

# Create a mask with green color for the edges
green_edges = np.zeros_like(original_image)
green_edges[edges != 0] = [0, 255, 0]  # Set the edges to green

# Superimpose the green edges onto the original image
#result_image = cv2.addWeighted(original_image, 1, green_edges, 1, 0)
result_image = cv2.addWeighted(original_image, 1, green_edges, 1, 0)

# Display the result
cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
