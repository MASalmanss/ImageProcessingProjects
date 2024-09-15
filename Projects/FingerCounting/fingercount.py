import cv2
import mediapipe as mp

# Video capture ayarları
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Mediapipe hands modülünü kullanmak için doğru şekilde çağır
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
tipId = [4 , 8 , 12 ,16 , 20]
while True:
    success, img = cap.read()

    if not success:
        break

    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRgb)

    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            for id , lm in enumerate(handLms.landmark):
                h , w, c = img.shape
                cx , cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id , cx ,cy])


    if len(lmList) != 0:
        fingers = []

        #Baş parmak
        if lmList[tipId[0]][1] < lmList[tipId[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # 4 parmak
        for id in range(1,5):
           if lmList[tipId[id]][2] <  lmList[tipId[id] - 2 ][2]:
               fingers.append(1)
           else:
                fingers.append(0)


        totalF = fingers.count(1)
        cv2.putText(img , str(totalF) , (30 ,125), cv2.FONT_HERSHEY_PLAIN , 10 , (255 , 0  , 0) , 2)

    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
