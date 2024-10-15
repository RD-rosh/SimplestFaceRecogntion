


# Simple Face Detection Using OpenCV

## Overview
This project demonstrates a basic face detection system using OpenCV's Haar Cascade Classifier. The system captures video from the default camera and detects faces in real-time. Faces are highlighted by green rectangles.

## Requirements
Make sure you have Python installed along with the following libraries:

- `opencv-python`

You can install the required libraries using the following command:

```bash
pip install opencv-python
```

## Code Explanation

### Importing Libraries
```python
import cv2
```
We are using the `opencv-python` library to handle the camera feed and process images for face detection.

### Exit Condition
```python
if key == 27:  # Press 'ESC' to exit
    break
```
The loop will break when the 'ESC' key is pressed.

### Releasing the Camera
```python
cam.release()
cv2.destroyAllWindows()
```
After exiting the loop, the camera is released and all OpenCV windows are closed.

## Running the Code
1. Save the code in a Python file, e.g., `face_detection.py`.
2. Run the script from the command line:
   ```bash
   python face_detection.py
   ```
3. The camera window will open, and it will start detecting faces in real-time. Press `ESC` to close the application.

## Notes
- Ensure that your computer has a webcam connected and accessible.
- The face detection works best in well-lit environments where the face is clearly visible.
- If you are using this code on a laptop, it usually uses the built-in webcam as the default camera.

<img width="1440" alt="Screenshot 2024-10-15 at 20 23 34" src="https://github.com/user-attachments/assets/07ca5527-0d6d-4a68-806e-f3d0a8ad11a8">


<img width="1440" alt="Screenshot 2024-10-15 at 20 30 13" src="https://github.com/user-attachments/assets/76d8681d-ecf8-4275-84a9-b0b53bf9c377">


```
