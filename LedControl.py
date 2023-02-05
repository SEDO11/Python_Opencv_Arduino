import cv2
import HandTrakingModule as htm
import pyfirmata as pf

# arduino 변수
port = 'COM3'
pwm = 25
ard = pf.Arduino(port)
pin3 = ard.get_pin('d:3:p')
pin5 = ard.get_pin('d:5:p')
pin6 = ard.get_pin('d:6:p')
pin9 = ard.get_pin('d:9:p')
pin11 = ard.get_pin('d:11:p')

# opencv 변수
wCam, hCam = 640, 480 # 창 가로, 세로 길이 변수

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, wCam) # 창 가로 길이
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, hCam) # 창 세로 길이

fps = htm.FPS()
detector = htm.HandDetector(maxHands=1)

def upFingerDrawing(x, y, b=255, g=0, r=255, scale=10):
    cv2.circle(img, (x, y), scale, (b, g, r), cv2.FILLED)

while True:
    # 1. find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findpostion(img, blue=0, green=0, red=150)

    # 2. get the tip of the index and middle fingers
    if len(lmList)!=0:
        x1, y1 = lmList[4][1:] # 엄지 끝 부분 좌표
        x2, y2 = lmList[8][1:] # 검지 끝 부분 좌표
        x3, y3 = lmList[12][1:] # 중지 끝 부분 좌표
        x4, y4 = lmList[16][1:] # 약지 끝 부분 좌표
        x5, y5 = lmList[20][1:] # 소지 끝 부분 좌표

        # 3. check which fingers are up
        fingers = detector.fingersUp()

        # 4. both index and middle fingers are up : clicking mode
        if fingers[0]==1: # 엄지를 올릴 경우
            upFingerDrawing(x1, y1)
            pin3.write(pwm)
        else:
            pin3.write(0)
            
        if fingers[1] == 1: # 검지를 올릴 경우
            upFingerDrawing(x2, y2)
            pin5.write(pwm)
        else:
            pin5.write(0)
            
        if fingers[2]==1: # 중지를 올릴 경우
            upFingerDrawing(x3, y3)
            pin6.write(pwm)
        else:
            pin6.write(0)
            
        if fingers[3] == 1: # 약지를 올릴 경우
            upFingerDrawing(x4, y4)
            pin9.write(pwm)
        else:
            pin9.write(0)
            
        if fingers[4] == 1: # 소지를 올릴 경우
            upFingerDrawing(x5, y5)
            pin11.write(pwm)
        else:
            pin11.write(0)
    # 11. frame rate
    fps.get_fps(img, blue=200, green=0, red=0)

    # 12. display
    if not success: # 카메라가 없으면 종료
        break

    cv2.imshow("camera", img)
    if cv2.waitKey(1) == ord('q'): # 사용자가 q를 입력한 경우 종료
        break

cap.release()
cv2.destroyAllWindows()