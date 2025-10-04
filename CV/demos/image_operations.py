"""
image_operations.py

Demo: Basic image operations with OpenCV.
- Read an image
- Resize
- Crop
- Draw simple shapes (line, rectangle, circle)
- Add text

Run:
    python image_operations.py

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
    img = load_image("Resources/img1.jpg")
    if img is None:
        return

    # Resize the image
    img_resized = cv.resize(img, (300, 200))

    # Crop a region of interest (ROI)
    img_cropped = img[50:200, 100:300]

    # Draw shapes on a copy
    img_draw = img.copy()
    cv.line(img_draw, (0, 0), (img.shape[1], img.shape[0]), (255, 0, 0), 3)
    cv.rectangle(img_draw, (50, 50), (200, 150), (0, 255, 0), 2)
    cv.circle(img_draw, (300, 200), 50, (0, 0, 255), -1)
    cv.putText(img_draw, "OpenCV Demo", (50, img.shape[0] - 20),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Show results
    cv.imshow("Original", img)
    cv.imshow("Resized", img_resized)
    cv.imshow("Cropped", img_cropped)
    cv.imshow("Drawn Shapes", img_draw)

    cv.waitKey(0)
    cv.destroyAllWindows()


# ---------------------------
# Entry point
# ---------------------------
if __name__ == "__main__":
    run_demo()
