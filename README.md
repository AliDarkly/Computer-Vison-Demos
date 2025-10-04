# Computer Vision Demos

This project contains multiple demos to learn and showcase basic concepts in **Computer Vision** using **OpenCV** and **Python**.

## Folder Structure

```
demos/
├─ image_operations.py       # Basic image operations: read, resize, crop, draw shapes & text
├─ filters_edges.py          # Applying filters and edge detection (Blur, Canny, Dilate, Erode)
├─ perspective_warp.py       # Perspective transform using 4 points
├─ shape_recognition.py      # Detecting and labeling basic shapes (triangle, square, circle...)
├─ face_detection.py         # Face detection using Haar Cascade
├─ plate_detection.py        # License plate detection using Haar Cascade
├─ color_detection.py        # Real-time color detection with webcam (using HSV ranges)
├─ virtual_painter.py        # Virtual painting using tracked color objects
├─ image_processing_demo.py  # Basic image processing pipeline demonstration
├─ grid_display_demo.py      # Display multiple images in a grid layout

Resources/                  # Images and videos used in demos
Xmls/                       # Haar Cascades (for face and plate detection)
```

## Installation

```bash
pip install opencv-python numpy
```

## How to Run Each Demo

### 1. Image Operations

```bash
python demos/image_operations.py
```

* Read and display an image
* Resize and crop operations
* Draw line, rectangle, circle, and text

### 2. Filters & Edge Detection

```bash
python demos/filters_edges.py
```

* Apply Gaussian Blur
* Edge detection using Canny
* Morphological operations: Dilation and Erosion

### 3. Perspective Warp

```bash
python demos/perspective_warp.py
```

* Select 4 points on the image with mouse clicks
* Warp the perspective to a flat view

### 4. Shape Recognition

```bash
python demos/shape_recognition.py
```

* Detect contours in an image
* Classify shapes (triangle, rectangle, square, circle)
* Label detected shapes

### 5. Face Detection

```bash
python demos/face_detection.py
```

* Detect faces using Haar Cascade
* Draw rectangles around detected faces

### 6. Plate Detection

```bash
python demos/plate_detection.py
```

* Detect license plates using Haar Cascade
* Highlight detected plates with rectangles and labels

### 7. Color Detection

```bash
python demos/color_detection.py
```

* Real-time color detection with webcam
* Adjust HSV thresholds using trackbars
* Display masked output

### 8. Virtual Painter

```bash
python demos/virtual_painter.py
```

* Track objects of a specific color
* Draw virtual circles on the screen following the tracked object

### 9. Image Processing Demo

```bash
python demos/image_processing_demo.py
```

* Apply Gaussian Blur, Canny, Dilation, and Erosion
* Show results in separate windows

### 10. Grid Display Demo

```bash
python demos/grid_display_demo.py
```

* Display multiple images in a grid (2x2)
* Automatically resize images for consistency

## Notes

* Place all images and videos in the `Resources/` folder.
* Haar Cascade XML files must be inside the `Xmls/` folder.
* For webcam-based demos, make sure your webcam is connected and accessible.
* All codes include English comments for readability and are structured for easy use in GitHub projects.
