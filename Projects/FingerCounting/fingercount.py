import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

while True:
    succes , frag = cap.read()

    if (succes != True):
        break

    cv2.imshow("img" , frag)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break