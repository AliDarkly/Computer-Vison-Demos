"""
perspective_warp.py

Demo: Perspective transform (warp) with OpenCV.

Features:
- Load an example image
- Two modes to obtain source points:
    1) Interactive: click 4 points on the image in the order you want
    2) Fallback: use a predefined set of source points
- Compute perspective transform and show warped image

Run:
    python perspective_warp.py

Notes:
    - Click exactly 4 points in interactive mode and then press 'w' to perform warp.
    - Press 'r' to reset selected points, 'q' to quit.

Requirements:
    - OpenCV (cv2)
    - numpy
"""

import cv2 as cv
import numpy as np
import os

# ---------------------------
# Utility: safe image loader
# ---------------------------

def load_image(path):
    """Load image from disk. Return None if file not found."""
    if not os.path.exists(path):
        print(f"[WARN] image not found: {path}")
        return None
    img = cv.imread(path)
    if img is None:
        print(f"[WARN] cv.imread failed for: {path}")
    return img


# ---------------------------
# Interactive point selector
# ---------------------------
POINTS = []


def mouse_callback(event, x, y, flags, param):
    """Mouse callback that collects up to 4 points on left-button clicks."""
    global POINTS
    if event == cv.EVENT_LBUTTONDOWN:
        if len(POINTS) < 4:
            POINTS.append((x, y))
            print(f"Point added: {(x, y)}")
        else:
            print("Already have 4 points. Press 'r' to reset.")


# ---------------------------
# Perspective warp function
# ---------------------------

def warp_perspective(src_img, src_pts, dst_size=(500, 500)):
    """
    Compute and apply a perspective transform.

    Args:
        src_img (np.ndarray): source image
        src_pts (list of tuple): 4 source points (x,y) in source image
        dst_size (tuple): (width, height) of the output warped image

    Returns:
        np.ndarray: warped image
    """
    if len(src_pts) != 4:
        raise ValueError("src_pts must contain 4 points")

    width, height = dst_size
    # Order points as float32 array
    pts1 = np.float32(src_pts)
    # Destination points: full rectangle
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    matrix = cv.getPerspectiveTransform(pts1, pts2)
    warped = cv.warpPerspective(src_img, matrix, (width, height))
    return warped


# ---------------------------
# Main demo
# ---------------------------

def run_demo():
    """Run the interactive perspective warp demo."""
    global POINTS

    img = load_image(os.path.join('Resources', 'perspective.jpg'))
    if img is None:
        print("perspective.jpg not found in Resources/. Exiting.")
        return

    clone = img.copy()
    window_name = 'Perspective Warp - click 4 points'
    cv.namedWindow(window_name)
    cv.setMouseCallback(window_name, mouse_callback)

    print("Interactive mode: click 4 points (corners) on the source image.")
    print("Press 'w' to warp, 'r' to reset points, 'q' to quit.")

    while True:
        disp = clone.copy()
        # draw selected points
        for i, p in enumerate(POINTS):
            cv.circle(disp, p, 5, (0, 255, 0), -1)
            cv.putText(disp, str(i + 1), (p[0] + 5, p[1] - 5), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv.imshow(window_name, disp)
        key = cv.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('r'):
            POINTS = []
            print("Points reset")
        elif key == ord('w'):
            if len(POINTS) == 4:
                try:
                    warped = warp_perspective(img, POINTS, dst_size=(500, 500))
                    cv.imshow('Warped Result', warped)
                    cv.imwrite('outputs/warped_result.jpg', warped) if os.path.isdir('outputs') else None
                    print('Warp applied. Press any key on warped window or continue interacting.')
                except Exception as e:
                    print('Error during warp:', e)
            else:
                print('Need 4 points to perform warp. Currently:', len(POINTS))

    cv.destroyAllWindows()


if __name__ == '__main__':
    run_demo()
