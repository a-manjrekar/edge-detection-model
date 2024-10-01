import cv2
import numpy as np

def edge_detection(image):
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  edges = cv2.Canny(gray, 50, 150)
  return edges

# Load the image
image = cv2.imread("Trex.jpg")

# Perform edge detection
edges = edge_detection(image)

# Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
