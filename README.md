# Hand Gesture Brightness Control

A Python-based project that controls system screen brightness using hand gestures through a webcam.

## Features
- Detects hand movements in real time
- Uses distance between fingers to control brightness
- Smooth brightness changes
- Displays brightness percentage on screen

## Technologies Used
- Python
- OpenCV
- CVZone
- NumPy
- screen-brightness-control

## How it Works
The webcam captures your hand.  
The distance between your thumb and index finger is measured.  
That distance is converted into a brightness value.

## How to Run
1. Install required libraries:
pip install opencv-python cvzone numpy screen-brightness-control

2. Run the program:
python brightness_control.py

## Use Case
Demonstrates real-time computer vision and gesture-based system control using Python.

## Author
Aleena Sahoo
