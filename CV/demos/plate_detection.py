"""
plate_detection.py

Demo: Detect vehicle number plates using Haar Cascade classifier in OpenCV.

Features:
- Load webcam feed
- Convert frames to grayscale
- Detect number plates using pre-trained Haar Cascade
- Draw rectangles and label around detected plates

Run:
    python plate_detection.py

Requirements:
    - OpenCV (cv2)
    - numpy
    - Xmls/haarcascade_russian_plate_number.xml
"""

import cv2 as cv
import os


def get_webcam():
    """Initialize webcam capture."""
    cam = cv.VideoCapture(0, cv.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)
    cam.set(10, 130)
    return cam


def run_demo():
    # Load Haar cascade for number plate detection
    plate_cascade_path = os.path.join('Xmls', 'haarcascade_russian_plate_number.xml')
    if not os.path.exists(plate_cascade_path):
        print(f"Haar cascade not found: {plate_cascade_path}")
        return
    plate_cas = cv.CascadeClassifier(plate_cascade_path)

    cam = get_webcam()

    print("Press 'q' to quit")

    while True:
        success, frame = cam.read()
        if not success:
            print("Error reading frame from webcam")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        plates = plate_cas.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in plates:
            area = w * h
            if area > 500:  # filter small detections
                cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv.putText(frame, 'Number Plate', (x, y - 5), cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

        cv.imshow('Plate Detection', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    run_demo()