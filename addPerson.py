import cv2 as cv
import pandas as pd
import os
import numpy as np
from addRecord import AddRecords

flag = 1
cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
newframe = []


def captureImage(event, x, y, flags, params):
    global flag, newframe
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)
        if x in range(250, 400) and y in range(400, 450):
            newframe = frame
            flag = 0


while flag:
    ret, frame1 = cap.read()
    # cv.namedWindow("frame")

    frame = np.array(frame1, copy=True)

    gray = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)

    faces = face_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 4)
        
    cv.rectangle(frame1, (250, 400), (400, 450), (200, 200, 200), -1)

    cv.putText(frame1, "Capture", (255, 430), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv.imshow("frame", frame1)

    cv.setMouseCallback("frame", captureImage)

    if cv.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

if flag == 0:
    ar = AddRecords()
    ar.takeInput()
    name = ar.fillInfo()
    os.chdir("People")
    cv.imwrite(f'{name}.jpg', newframe)
