#-------------main--------------------------
def main():
    cTime=0
    pTime=0
    cap = cv2.VideoCapture(0)
    while True:
        success,img = cap.read()
        # class object
        detector = handdetector()
        img = detector.findhands(img)
        position = detector.findPosition(img)

        if len(position)!=0:
            print(position)


        # calculating time
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),1)

        cv2.imshow('img',img)
        if cv2.waitKey(20) & 0xFF == ord('d'):
            break

#-----------------python main---------------
if __name__=="__main__":
    main()