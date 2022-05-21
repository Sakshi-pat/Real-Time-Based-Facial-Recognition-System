import cv2 as cv
from simple_facerec import SimpleFacerec
from viewDetails import ViewDetails

sfr = SimpleFacerec()
sfr.load_encoding_images('People/')


def getDetails(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        if x in range(250, 400) and y in range(400, 450):
            print(face_name)
            vd = ViewDetails(face_name)


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()

    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, face_name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc
        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv.FILLED)
        cv.putText(frame, face_name, (x1 + 6, y2 - 6), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv.rectangle(frame, (250, 400), (450, 450), (200, 200, 200), -1)

    cv.putText(frame, "Get Details", (255, 430), cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv.imshow('frame', frame)

    cv.setMouseCallback("frame", getDetails)

    if cv.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
