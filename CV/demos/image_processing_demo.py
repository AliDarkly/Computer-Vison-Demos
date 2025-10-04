"""
image_processing_demo.py

Demo: Basic image processing operations using OpenCV.

Features:
- Read images from disk
- Apply Gaussian blur
- Edge detection using Canny
- Dilation and erosion
- Show processed images

Run:
    python image_processing_demo.py

Requirements:
    - OpenCV (cv2)
    - numpy
"""

import cv2 as cv
import numpy as np


def load_image(path, color=cv.IMREAD_COLOR):
    img = cv.imread(path, color)
    if img is None:
        print(f"[WARN] Could not read image: {path}")
    return img


def run_demo():
    # Load image
    img = load_image('Resources/img3.jpg')
    if img is None:
        return

    # Apply Gaussian blur
    img_blur = cv.GaussianBlur(img, (7, 7), 0)

    # Edge detection using Canny
    img_canny = cv.Canny(img, 50, 50)

    # Create kernel for dilation and erosion
    kernel = np.ones((5,5), np.uint8)

    # Dilation
    img_dilate = cv.dilate(img_canny, kernel, iterations=1)

    # Erosion
    img_erode = cv.erode(img_dilate, kernel, iterations=1)

    # Show results
    cv.imshow('Original', img)
    cv.imshow('Blur', img_blur)
    cv.imshow('Canny', img_canny)
    cv.imshow('Dilation', img_dilate)
    cv.imshow('Erosion', img_erode)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    run_demo()