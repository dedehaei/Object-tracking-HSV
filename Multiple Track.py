import numpy as np 
import cv2 
webcam = cv2.VideoCapture(0) 
while(1):
    h = int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
    w = int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(str(h) + str(w))
    _, imageFrame = webcam.read()
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    kernal = np.ones((5, 5), "uint8")

    

    bola_lower = (0,136,110)
    bola_upper = (12,252,212)
    bola_mask = cv2.inRange(hsvFrame, bola_lower, bola_upper)
    bola_mask = cv2.dilate(bola_mask, kernal)
    bola_mask = cv2.medianBlur(bola_mask,7)
    res_bola = cv2.bitwise_and(imageFrame, imageFrame, mask = bola_mask) 

    magenta_lower = (137,77,120)
    magenta_upper = (175,157,255)
    magenta_mask = cv2.inRange(hsvFrame, magenta_lower, magenta_upper)
    magenta_mask = cv2.dilate(magenta_mask, kernal)
    magenta_mask = cv2.medianBlur(magenta_mask,7)
    res_magenta = cv2.bitwise_and(imageFrame, imageFrame, mask = magenta_mask)

    cyan_lower = (100,50,98)
    cyan_upper = (117,123,183)
    cyan_mask = cv2.inRange(hsvFrame, cyan_lower, cyan_upper)
    cyan_mask = cv2.dilate(cyan_mask, kernal)
    cyan_mask = cv2.medianBlur(cyan_mask,7)
    res_cyan = cv2.bitwise_and(imageFrame, imageFrame, mask = cyan_mask)

    contours, hierarchy = cv2.findContours(bola_mask, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 1000):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h),
                                       (0, 165, 255), 2)
            cv2.putText(imageFrame, "Bola " + str(x) + ","+str(y), (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 165, 255))
            print('Bola : ',int(area))

    contours, hierarchy = cv2.findContours(magenta_mask, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)  
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 10000):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h),
                                       (0,0,255), 2)
            cv2.putText(imageFrame, "Magenta", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,0,255))
            print('Magenta : ',area)
            
    contours, hierarchy = cv2.findContours(cyan_mask, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE) 
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 10000):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h),
                                       (255, 0, 0), 2)
            cv2.putText(imageFrame, "Cyan" + str(x) +","+str(y), (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
            print('cyan : ',int(area))
            
    cv2. line(imageFrame ,((int(w/3)-1),int(0)),((int(w/3)-1),int(h)),(255,0,0),1)
    cv2. line(imageFrame ,((int(w/3*2)-1),int(0)),((int(w/3*2)-1),int(h)),(255,0,0),1)
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    
    #cv2.imshow('Bola',res_bola)
    #cv2.imshow('Magenta',res_magenta)
    #cv2.imshow('Cyan',res_cyan)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break
