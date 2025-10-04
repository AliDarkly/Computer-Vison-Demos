"""
grid_display_demo.py

Demo: Display multiple images in a grid layout using OpenCV and numpy.

Features:
- Resize images to same dimensions
- Convert grayscale images to BGR for consistency
- Combine multiple images into a single grid
- Display the resulting grid

Run:
    python grid_display_demo.py

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


def create_grid(images, rows, cols):
    if len(images) != rows * cols:
        raise ValueError("rows * cols must be equal to number of images")

    # Resize and convert grayscale images to BGR
    h, w = images[0].shape[:2]
    fixed_imgs = []
    for img in images:
        if len(img.shape) == 2:
            img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        img = cv.resize(img, (w, h))
        fixed_imgs.append(img)

    grid_rows = []
    for r in range(rows):
        row_imgs = fixed_imgs[r*cols:(r+1)*cols]
        row = np.hstack(row_imgs)
        grid_rows.append(row)

    grid = np.vstack(grid_rows)
    return grid


def run_demo():
    img1 = load_image('Resources/img1.jpg')
    img2 = load_image('Resources/img2.jpg')
    img3 = load_image('Resources/img3.jpg')
    img4 = load_image('Resources/paper.jpg')

    images = [img1, img2, img3, img4]

    grid_img = create_grid(images, 2, 2)

    cv.imshow('Image Grid', grid_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    run_demo()