"""
Hand Gesture Brightness Control
Author: Aleena Sahoo
Description: Control system brightness using finger distance
"""
import cv2
from cvzone.HandTrackingModule import HandDetector
from math import hypot
import numpy as np
import screen_brightness_control as sbc

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)

while True:
    success, frame = cap.read()
    if not success:
        break

    # Detect hands
    hands, frame = detector.findHands(frame)

    if hands:
        # Get the first detected hand
        lmList = hands[0]["lmList"]

        # Thumb tip and Index tip landmark points
        x1, y1 = lmList[4][0], lmList[4][1]   # Thumb tip
        x2, y2 = lmList[8][0], lmList[8][1]   # Index finger tip

        # Draw circles and line
        cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
        cv2.circle(frame, (x2, y2), 10, (255, 0, 0), -1)
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)

        # Calculate distance between two fingers
        distance = hypot(x2 - x1, y2 - y1)

        # Map distance to brightness level (adjust values as needed)
        brightness = np.interp(distance, [30, 200], [10, 100])
        brightness = int(brightness)

        # Set screen brightness
        sbc.set_brightness(brightness)

        # Display brightness on screen
        cv2.putText(frame, f'Brightness: {brightness}%', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show video feed
    cv2.imshow("Brightness Control", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
