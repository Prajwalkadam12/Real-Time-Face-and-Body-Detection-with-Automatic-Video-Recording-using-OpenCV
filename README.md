CCTV Camera Surveillance with OpenCV
This project is a simple Python-based CCTV camera surveillance system that captures video using your webcam. It detects faces and bodies using Haar Cascade classifiers and automatically records video when any faces or bodies are detected. The recording stops a few seconds after the last detection.

Requirements
To run this project, you need to have the following installed on your machine:

Python 3.x
OpenCV (cv2)
You can install OpenCV via pip:

bash
Copy code
pip install opencv-python
Project Overview
The system works as follows:

The webcam captures video in real-time.
The Haar Cascade classifiers are used to detect faces and bodies in the frame.
If a face or body is detected, the system starts recording the video and saves it in .mp4 format.
If no face or body is detected for 5 seconds (configurable), the system stops recording.
The video is saved with a timestamp in the filename.
The system continues to monitor the feed, and recording resumes if another detection is made.
Key Features
Real-Time Detection: Detects faces and bodies in real-time using the webcam.
Automatic Recording: Records video only when a face or body is detected.
Timed Recording: Continues recording for 5 seconds after the last detection.
Easy Exit: You can exit the program by pressing the q key.
Save Videos: Each recording is saved with a timestamp as the filename.
Usage
Clone the repository or download the script.

Ensure the required packages are installed (OpenCV).

Run the script:

bash
Copy code
python surveillance.py
The webcam window will appear, and it will begin monitoring for faces or bodies. Once detected, it will start recording video.

To stop the script, press q in the webcam window.

Code Breakdown
Video Capture: The webcam feed is captured using cv2.VideoCapture().
Detection: Faces and bodies are detected using Haar Cascade classifiers (haarcascade_frontalface_default.xml and haarcascade_fullbody.xml).
Recording: Video is recorded using cv2.VideoWriter() when faces or bodies are detected. The filename is generated using the current timestamp.
Timer: After the last detection, the system waits for 5 seconds before stopping the recording, ensuring that brief interruptions do not prematurely stop the video.
Exit: The program can be exited by pressing the q key.
File Structure
plaintext
Copy code
surveillance.py    # The main script for the CCTV camera
Customization
You can customize the following parameters in the script:

Recording Duration After Detection: Modify SECONDS_TO_RECORD_AFTER_DETECTION to change how long the system continues recording after the last detection (default is 5 seconds).
Detection Sensitivity: The scaleFactor and minNeighbors in the detectMultiScale() method can be adjusted to fine-tune the sensitivity of face and body detection.
Video Format and Frame Size: The frame size and video codec can be modified when initializing cv2.VideoWriter().
References
OpenCV Documentation
Haar Cascade Classifiers
License
This project is free to use for personal and educational purposes.
