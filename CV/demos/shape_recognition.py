"""
shape_recognition.py

Demo: Detect contours and recognize simple shapes with OpenCV.

Features:
- Convert image to grayscale
- Apply blur and edge detection
- Find contours
- Approximate polygon and detect shape type (triangle, rectangle, circle, etc.)
- Draw contours and labels on the image

Run:
    python shape_recognition.py

Requirements:
    - OpenCV (cv2)
    - numpy
"""

import cv2 as cv
import numpy as np


def load_image(path):
    """Load image safely from disk."""
    img = cv.imread(path)
    if img is None:
        print(f"[WARN] Could not read image: {path}")
    return img


def get_contours(img):
    """
    Find contours, approximate shapes and draw them on a copy of the image.
    """
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img_gray, (5, 5), 1)
    img_canny = cv.Canny(img_blur, 50, 150)

    contours, _ = cv.findContours(img_canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    img_contour = img.copy()

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:  # filter noise
            cv.drawContours(img_contour, [cnt], -1, (255, 0, 0), 2)

            # perimeter and polygon approx
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)

            x, y, w, h = cv.boundingRect(approx)

            shape_type = "Unknown"
            obj_cor = len(approx)
            asp_ratio = w / float(h)
            if obj_cor == 3:
                shape_type = "Triangle"
            elif obj_cor == 4:
                if 0.95 < asp_ratio < 1.05:
                    shape_type = "Square"
                else:
                    shape_type = "Rectangle" 
            elif obj_cor == 5 :
                shape_type = "Pentagon"
            elif obj_cor == 10 :
                shape_type = "Star"
            elif obj_cor ==6 :
                shape_type = "Hexagon"
            elif obj_cor > 4:
                if 0.95 < asp_ratio < 1.05:
                    shape_type = "Circle"
                else:
                    shape_type = "Oval" 

            
            cv.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(img_contour, shape_type, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX,
                       0.7, (0, 255, 0), 2)

    return img_contour


def run_demo():
    img = load_image("Resources/shapes.jpg")
    if img is None:
        return

    img_result = get_contours(img)

    cv.imshow("Original", img)
    cv.imshow("Shape Recognition", img_result)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    run_demo()