#!/opt/local/bin/python

import cv2
import sys
from textReminder import send_text_reminder

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

# capture 4 frames
nframes = 4

counter = 0

for i in range(0,nframes):
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    if len(faces) != 0:
        counter += 1
   
# if you count faces in less than half the nframes, send a reminder
if(counter < nframes/2):
    send_text_reminder()

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()