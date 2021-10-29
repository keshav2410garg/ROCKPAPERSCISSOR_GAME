import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import time
from tkinter import messagebox
from tkinter import*


cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
root = Tk()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    k=cv2.waitKey(1)
    cv2.line(frame,(650,0),(650,900),(255,255,255),2)
    cv2.rectangle(frame,(100,100),(500,500),(255,255,255),2)#Drawing the first rectangle for player 1
    cv2.rectangle(frame,(800,100),(1200,500),(255,255,255),2)#Drawing the second rectangle for player two
    cv2.putText(frame, "PLAYER 1", (50, 600), cv2.FONT_HERSHEY_SIMPLEX, 2,(255,255,255),2)
    cv2.putText(frame, "PLAYER 2", (700, 600), cv2.FONT_HERSHEY_SIMPLEX, 2,(255,255,255),2)
    cv2.imshow('frame',frame)
    if k%256==32: #Gesture will n
        img_name1="firstplayergesture.png"
        firstp=frame[100:500,100:500]
        cv2.imwrite(img_name1,firstp)
        img_name2="secondplayergesture.png"
        secondp=frame[100:500,800:1200]
        cv2.imwrite(img_name2,secondp)
        firstp= cv2.imread('D:firstplayergesture.png')
        secondp= cv2.imread('D:secondplayergesture.png')
        
        firstp=cv2.GaussianBlur(firstp,(5,5),0)
        secondp=cv2.GaussianBlur(secondp,(5,5),0)
        
        cv2.imshow('first player gesture',firstp)
        cv2.imshow('second player gesture',secondp)
        
        #First Player Gesture
        hsv1=cv2.cvtColor(firstp,cv2.COLOR_BGR2HSV)
        lower_skin=np.array([0,30,60])
        upper_skin=np.array([20,150,255])
        
        first_binary=cv2.inRange(hsv1,lower_skin,upper_skin)#binary image for first player gesture
        
        kernel=np.ones((3,3),np.uint8)
        
        dilution1=cv2.dilate(first_binary,kernel,iterations=1)
        erosion1=cv2.erode(dilution1,kernel,iterations=1)

        ret1,the1=cv2.threshold(erosion1,70,255,cv2.THRESH_BINARY)
        #cv2.imshow('Firstp threshold',the1)
        
        contours1,hierarchy=cv2.findContours(the1.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        max_area = -1
        for i in range(len(contours1)):
            area = cv2.contourArea(contours1[i])
            if area>max_area:
                cnt = contours1[i]
                max_area = area
        cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        
        cv2.drawContours(firstp, cnt, 0, (0, 255, 0), 3)
        #cv2.imshow("Contoured_image1",firstp)
        
        hull=cv2.convexHull(cnt,returnPoints=False)
        defects=cv2.convexityDefects(cnt,hull)
        count_defects=0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            #If the angle of hand is changed
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14
                
            if angle <= 90:
                count_defects += 1
                cv2.circle(firstp, far, 1, [0, 0, 255], -1)
                cv2.line(firstp, start, end, [0, 255, 0], 2)
        p1_gesture=""        
        #Print the Gestures
        if count_defects == 0:
            p1_gesture="Stone"
            cv2.putText(frame, "Stone", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
            cv2.imshow('frame',frame)
            cv2.waitKey()
        elif count_defects == 1:
            p1_gesture="Scissor"
            cv2.putText(frame, "Scissor", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            cv2.imshow('frame',frame)
            cv2.waitKey()
        elif count_defects == 4:
            p1_gesture="Paper"
            cv2.putText(frame, "Paper", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            cv2.imshow('frame',frame)
            cv2.waitKey()
        else:
            pass
        
        #print("first player contours",count_defects)
        
        
        #Second Player Gesture
        hsv2=cv2.cvtColor(secondp,cv2.COLOR_BGR2HSV)
        lower_skin=np.array([0,30,60])
        upper_skin=np.array([20,150,255])

        kernel=np.ones((3,3),np.uint8)
        
        second_binary=cv2.inRange(hsv2,lower_skin,upper_skin)#binary image for first player gesture
        dilution2=cv2.dilate(second_binary,kernel,iterations=1)
        erosion2=cv2.erode(dilution2,kernel,iterations=1)
        
        ret2,the2=cv2.threshold(erosion2,70,255,cv2.THRESH_BINARY)
        #cv2.imshow('Secondp threshold',the2)
        contours2,hierarchy=cv2.findContours(the2.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        max_area = -1
        for i in range(len(contours2)):
            area = cv2.contourArea(contours2[i])
            if area>max_area:
                cnt = contours2[i]
                max_area = area
        cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        
        cv2.drawContours(secondp, cnt, 0, (0, 255, 0), 3)
        #cv2.imshow("contoured_image2",secondp)
        
        hull=cv2.convexHull(cnt,returnPoints=False)
        defects=cv2.convexityDefects(cnt,hull)

        count_defects=0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            #If the angle of hand is changed
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14
                
            if angle <= 90:
                count_defects += 1
                cv2.circle(secondp, far, 1, [0, 0, 255], -1)
                cv2.line(secondp, start, end, [0, 255, 0], 2)
        p2_gesture=""
        #Print the Gestures
        if count_defects == 0:
            p2_gesture="Stone"
            cv2.putText(frame, "Stone", (655, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2)
            cv2.imshow('frame',frame)
            cv2.waitKey()
        elif count_defects == 1:
            p2_gesture="Scissor"
            cv2.putText(frame, "Scissor", (655, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            cv2.imshow('frame',frame)
            cv2.waitKey()
        elif count_defects == 4:
            p2_gesture="Paper"
            cv2.putText(frame, "Paper", (655, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255), 2)
            cv2.imshow('frame',frame)
            cv2.waitKey()
        else:
            pass


        #print("second player contours ",count_defects)
 
        if (p1_gesture=="Stone" and p2_gesture=="Scissor") or (p1_gesture=="Scissor" and p2_gesture=="Paper") or (p1_gesture=="Paper" and p2_gesture=="Stone"):
            print("Player 1 wins!")
            messagebox.showinfo("Winner", "Player 1 is the winner")
            root.mainloop() 
        elif (p2_gesture=="Stone" and p1_gesture=="Scissor") or (p2_gesture=="Scissor" and p1_gesture=="Paper") or (p2_gesture=="Paper" and p1_gesture=="Stone"):
            print("Player 2 wins!")
            messagebox.showinfo("Winner", "Player 2 is the winner")
            root.mainloop()
        elif (p1_gesture==p2_gesture):
            print("It's a Draw!")
            messagebox.showinfo("Winner", "It is a Draw")
            root.mainloop() 
        else:
            print("Error recording the gesture, try again!")
            messagebox.showinfo("Winner", "Error recording the gesture, try again!")
            root.mainloop() 
    if cv2.waitKey(1)==ord('q'):
        break

        
# Closing the video capture window on the press of Q
cap.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()
        