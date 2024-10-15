import cv2
import time
import datetime

# Initialize the webcam capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Load the face and body cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

# Variables for detection logic
detection = False
detection_stopped_time = None
timer_started = False
SECONDS_TO_RECORD_AFTER_DETECTION = 5

# Define video frame size and format
frame_size = (int(cap.get(3)), int(cap.get(4)))
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

while True:
    # Read the video frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces and bodies in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # If faces or bodies are detected, start recording
    if len(faces) + len(bodies) > 0:
        if detection:
            timer_started = False
        else:
            detection = True
            current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
            print("Started Recording!")

    # If no detection, handle the stop timer
    elif detection:
        if timer_started:
            if time.time() - detection_stopped_time >= SECONDS_TO_RECORD_AFTER_DETECTION:
                detection = False
                timer_started = False
                out.release()
                print("Stopped Recording!")
        else:
            timer_started = True
            detection_stopped_time = time.time()

    # If currently detecting, continue writing the video
    if detection:
        out.write(frame)

    # Show the frame in a window
    cv2.imshow("CCTV Camera", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release resources when done
cap.release()
if detection:  # Ensure the file is released if still recording
    out.release()
cv2.destroyAllWindows()
