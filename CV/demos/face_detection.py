"""
face_detection.py

Demo: Detect faces using Haar Cascade classifier in OpenCV.

Features:
- Load webcam feed
- Convert frames to grayscale
- Detect faces using pre-trained Haar Cascade
- Draw rectangles around detected faces

Run:
    python face_detection.py

Requirements:
    - OpenCV (cv2)
    - numpy
    - Xmls/haarcascade_frontalface_default.xml (Haar Cascade file)
"""

import cv2 as cv
import os


def get_webcam():
    """Initialize webcam capture."""
    cam = cv.VideoCapture(0, cv.CAP_DSHOW)
    cam.set(3, 640)
    cam.set(4, 480)
    cam.set(10, 130)  # brightness
    return cam


def run_demo():
    # Load Haar cascade for face detection
    face_cascade_path = os.path.join('Xmls', 'haarcascade_frontalface_default.xml')
    if not os.path.exists(face_cascade_path):
        print(f"Haar cascade not found: {face_cascade_path}")
        return
    face_cas = cv.CascadeClassifier(face_cascade_path)

    cam = get_webcam()

    print("Press 'q' to quit")

    while True:
        success, frame = cam.read()
        if not success:
            print("Error reading frame from webcam")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cas.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv.imshow('Face Detection', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    run_demo()