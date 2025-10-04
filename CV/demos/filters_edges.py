"""
filters_edges.py

Demo: Applying filters and edge detection with OpenCV.
- Gaussian Blur
- Canny Edge Detection
- Dilation
- Erosion

Run:
    python filters_edges.py

Requirements:
    - OpenCV (cv2)
    - numpy
"""

import cv2 as cv
import numpy as np

# ---------------------------
# Utility function: load image safely
# ---------------------------
def load_image(path):
    """Try to load an image from disk. Return None if not found."""
    img = cv.imread(path)
    if img is None:
        print(f"[WARN] Could not read image: {path}")
    return img


# ---------------------------
# Main demo function
# ---------------------------
def run_demo():
    # Load an example image (replace path with your file)
    img = load_image("Resources/img3.jpg")
    if img is None:
        return

    # Apply Gaussian blur
    img_blur = cv.GaussianBlur(img, (7, 7), 0)

    # Detect edges with Canny
    img_canny = cv.Canny(img, 50, 150)

    # Define kernel for morphology
    kernel = np.ones((5, 5), np.uint8)

    # Dilate edges
    img_dilate = cv.dilate(img_canny, kernel, iterations=1)

    # Erode edges
    img_erode = cv.erode(img_dilate, kernel, iterations=1)

    # Show results
    cv.imshow("Original", img)
    cv.imshow("Blurred", img_blur)
    cv.imshow("Canny Edges", img_canny)
    cv.imshow("Dilated", img_dilate)
    cv.imshow("Eroded", img_erode)

    cv.waitKey(0)
    cv.destroyAllWindows()


# ---------------------------
# Entry point
# ---------------------------
if __name__ == "__main__":
    run_demo()