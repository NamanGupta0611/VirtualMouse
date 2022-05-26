import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui
import autopy

##########################
wCam, hCam = 640, 480
frameR = 150 # Frame Reduction
smoothening = 7
########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands = 1,detectionCon=0.75, trackCon = 0.5)
wScr, hScr = autopy.screen.size()

while True:
    # 1. Find hand Landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x0, y0 = lmList[4][1:]
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)
    
        # 3. Check which fingers are up
        fingers = detector.fingersUp(img)
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
        (255, 0, 255), 2)
        
        # 4. Only Index Finger : Moving Mode
        if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        
            # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) // smoothening
            clocY = plocY + (y3 - plocY) // smoothening
        
            # 7. Move Mouse
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY
            
        # 8. Index Finger is also up : Left Click Mode
        if fingers[1] == 1 and fingers[0] == 1:
            # 9. Find distance between Thumb and Finger
            lengthL, img, line1Info = detector.findDistance(6, 4, img)
            print("Left click length : ",lengthL)
            # 10. Click mouse if distance short
            if lengthL < 40:
                cv2.circle(img, (line1Info[4], line1Info[5]),
                15, (0, 255, 0), cv2.FILLED)
                pyautogui.click(clicks = 1, button = "left")
        
        # 11. Both Index and middle finger are up : Right Click Mode
        if fingers[1] == 1 and fingers[2] == 1:
            lenghtR, img, line2Info = detector.findDistance(8, 12, img)
            print("Right Click length : ", lenghtR)
            #12. Click mouse distance if distance short
            if lenghtR < 40:
                cv2.circle(img, (line2Info[4], line2Info[5]), 15, (0, 255, 0), cv2.FILLED)
                pyautogui.rightClick()
    
    # 13. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    img = cv2.flip(img, 1)
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    (255, 0, 0), 3)
    # 14. Display
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()