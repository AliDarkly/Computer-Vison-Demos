"""
virtual_painter.py

Demo: Simple virtual painter using colored objects and webcam feed.

Features:
- Detect colors using predefined HSV ranges
- Track positions of colored objects
- Draw on screen following object movements

Run:
    python virtual_painter.py

Requirements:
    - OpenCV (cv2)
    - numpy
"""

import cv2 as cv
import numpy as np

# Predefined color ranges in HSV and BGR for drawing
myclr = [
    [35, 64, 0, 94, 255, 255],  # green
    [94, 120, 0, 146, 255, 255],  # blue
    [159, 125, 0, 179, 255, 227]  # red
]
myclrvals = [
    [0, 255, 0],  # green in BGR
    [255, 0, 0],  # blue
    [0, 0, 255]   # red
]

mypnts = []  # store points for drawing


def get_webcam():
    cam = cv.VideoCapture(0, cv.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)
    cam.set(10, 130)
    return cam


def get_highest_contours(img):
    contours, _ = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y = 0, 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 1000:
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x1, y1, w, h = cv.boundingRect(approx)
            x, y = x1 + w // 2, y1
    return x, y


def color_detect(frame, myclr, myclrvals, img_result):
    new_points = []
    imgHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    for idx, clr in enumerate(myclr):
        lower = np.array(clr[:3])
        upper = np.array(clr[3:6])
        mask = cv.inRange(imgHSV, lower, upper)
        x, y = get_highest_contours(mask)
        if x != 0 and y != 0:
            cv.circle(img_result, (x, y), 10, myclrvals[idx], cv.FILLED)
            new_points.append([x, y, idx])
    return new_points


def draw_on_canvas(points, myclrvals, img_result):
    for point in points:
        cv.circle(img_result, (point[0], point[1]), 10, myclrvals[point[2]], cv.FILLED)


def run_demo():
    cam = get_webcam()

    print("Virtual Painter Demo: Press 'q' to quit")

    while True:
        success, frame = cam.read()
        if not success:
            print("Error reading webcam")
            break

        img_result = frame.copy()
        new_points = color_detect(frame, myclr, myclrvals, img_result)

        if new_points:
            for p in new_points:
                mypnts.append(p)

        if mypnts:
            draw_on_canvas(mypnts, myclrvals, img_result)

        cv.imshow("Virtual Painter", img_result)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    run_demo()