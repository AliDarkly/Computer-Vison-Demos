"""
color_detection.py

Demo: Detect specific colors in webcam feed using HSV thresholds.

Features:
- Webcam feed
- Convert frames to HSV
- Use trackbars to dynamically adjust HSV min/max values
- Apply mask and display result

Run:
    python color_detection.py

Requirements:
    - OpenCV (cv2)
    - numpy
"""

import cv2 as cv
import numpy as np


def get_webcam():
    cam = cv.VideoCapture(0, cv.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)
    cam.set(10, 130)
    return cam


def empty(a):
    pass


def create_trackbars():
    cv.namedWindow('Trackbars')
    cv.resizeWindow('Trackbars', 640, 240)
    cv.createTrackbar('Hue min','Trackbars',0,179,empty)
    cv.createTrackbar('Hue max','Trackbars',179,179,empty)
    cv.createTrackbar('Sat min','Trackbars',0,255,empty)
    cv.createTrackbar('Sat max','Trackbars',255,255,empty)
    cv.createTrackbar('Val min','Trackbars',0,255,empty)
    cv.createTrackbar('Val max','Trackbars',255,255,empty)


def run_demo():
    cam = get_webcam()
    create_trackbars()

    print("Adjust the HSV trackbars. Press 'q' to quit.")

    while True:
        success, frame = cam.read()
        if not success:
            print("Error reading frame from webcam")
            break

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        h_min = cv.getTrackbarPos('Hue min','Trackbars')
        h_max = cv.getTrackbarPos('Hue max','Trackbars')
        s_min = cv.getTrackbarPos('Sat min','Trackbars')
        s_max = cv.getTrackbarPos('Sat max','Trackbars')
        v_min = cv.getTrackbarPos('Val min','Trackbars')
        v_max = cv.getTrackbarPos('Val max','Trackbars')

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        mask = cv.inRange(hsv, lower, upper)
        result = cv.bitwise_and(frame, frame, mask=mask)

        cv.imshow('Original', frame)
        cv.imshow('Mask', mask)
        cv.imshow('Result', result)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    run_demo()