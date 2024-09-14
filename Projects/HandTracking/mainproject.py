import cv2
import mediapipe 
import time

# Kamerayı başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera açılamadı. Lütfen cihazın bağlı olduğundan emin olun.")
    exit()


Mphands = mediapipe.solutions.hands

hands = Mphands.Hands(max_num_hands = 2)

mpDraw = mediapipe.solutions.drawing_utils
pTime = 0
cTime = 0
while True:
    success, img = cap.read()
    imgRgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
    results = hands.process(imgRgb)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img , landmarks , Mphands.HAND_CONNECTIONS)
            for id ,lm in enumerate(landmarks.landmark):
                print(id , lm)
                h , w , c = img.shape

                cx,cy = int(lm.x * w) , int(lm.y * h)

                if id == 0:
                    cv2.circle(img , (cx, cy) , 9 , (255 , 0 , 0) , cv2.FILLED)

    #fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img , "FPS : " + str(int(fps)) , (10 , 75) , cv2.FONT_HERSHEY_COMPLEX , 3 , (255 , 0 , 0) , 5)
    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera ve pencereleri serbest bırak
cap.release()
cv2.destroyAllWindows()