
import cv2

# Load Haar Cascade for face detection
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)  # 0 is usually the default camera

# Check if the camera opened successfully
if not cam.isOpened():
    print("Error: Could not open video stream.")
    exit()

#infinite loop for read frame from cam
while True:
    
    ret, img = cam.read()

    
    if not ret:
        print("Failed to capture image. Exiting...")
        break

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

    #Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Face Detection', img)

    #brk loop with ESC key
    key = cv2.waitKey(10)
    if key == 27:  # Press 'ESC' to exit
        break

cam.release()
cv2.destroyAllWindows()
