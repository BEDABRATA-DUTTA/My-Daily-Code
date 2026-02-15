import cv2

# Load Haar Cascade model
cas = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Start webcam
capvideo = cv2.VideoCapture(0)

while True:
    # Capture frame
    ret, cap_image = capvideo.read()

    # If frame not captured, exit
    if not ret:
        print("Failed to capture image")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(cap_image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = cas.detectMultiScale(gray, 1.3, 6)

    # Draw rectangle around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(cap_image, (x, y), (x + w, y + h), (255, 0, 0), 3)

    # Show camera window
    cv2.imshow("Face Detection", cap_image)

    # Wait for key press
    key = cv2.waitKey(1)

    # Stop conditions:
    # ord('q') = Q key
    # 27 = ESC key
    # 13 = ENTER key
    if key == ord('q') or key == 27 or key == 13:
        print("Stopping camera...")
        break

# Release webcam
capvideo.release()

# Close all windows
cv2.destroyAllWindows()


#ESC to stop