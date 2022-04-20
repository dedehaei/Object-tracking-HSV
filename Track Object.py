#from imutils.video import VideoStream
import cv2 
import numpy as np
import imutils
def nothing(x):
    pass

cap = cv2.VideoCapture(0) 
if (cap.isOpened()== False):  
  print("Error opening video  file") 

while(cap.isOpened()):       
  ret, frame = cap.read()
  if ret == True:
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    Lower = (22,108,125)
    Upper = (31,183,186)
    mask = cv2.inRange(hsv,Lower,Upper)
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations = 2)
    mask = cv2.medianBlur(mask, 7)
    mask = cv2.GaussianBlur(mask,(7,7),0)
    res = cv2.bitwise_and(frame,frame,mask = mask)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None
    if len(cnts) >0:
        c= max(cnts,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))

        if radius > 10 :
                  #cv2.circle(frame, (int(x),int(y)),int(radius),
                   #          (0,255,255),2)
                  print("Kordinat",int(x),",",int(y))
                  print("Radius",int(radius))
                  cv2.circle(frame,center,5,(0,0,255),-1)
    else:
        print("NOT DETECTING")
    cv2.imshow('Mask', mask)
    cv2.imshow('Original',frame)
    cv2.imshow('Result',res)
    if cv2.waitKey(25) & 0xFF == ord('q'): 
      break
   
  else:  
    break

cap.release() 

cv2.destroyAllWindows() 
