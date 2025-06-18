import cv2
import mediapipe as mp
import time

# class
class handdetector:
    def __init__(self,mode=False,maxHands=2,modelComplexity=1,detectionConf=0.5,trackingConf=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionConf = detectionConf
        self.trackingConf = trackingConf

        # detecting landmarks and connections
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,modelComplexity,detectionConf,trackingConf)
        self.mpdraw = mp.solutions.drawing_utils


    #-------------findhands----------------
    def findhands(self,img,draw=True):
        self.RGBimg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(self.RGBimg)

        if self.result.multi_hand_landmarks:
            for handlms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpdraw.draw_landmarks(img,handlms,self.mpHands.HAND_CONNECTIONS)

        return img

    # finding position=====================
    def findPosition(self, img, handNo=0, draw=True):

        lmlist = []

        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)

        return lmlist
    


    