import cv2
import time
import numpy as np



cap=cv2.VideoCapture(0)

img=cv2.imread("img.png")

while(True):
    ret,frame=cap.read()
    print(frame)
    frame=cv2.resize(frame,(640,480))
    img=cv2.resize(img,(640,480))
    
    lower_red=np.array([104,153,70])
    upper_red=np.array([30,30,0])
    mask_1=cv2.inRange(frame,lower_red,upper_red)
    
    
    res_1=cv2.bitwise_and(frame,frame,mask=mask_1)
    f=frame-res_1
    f=np.where(f==0,img,f)  
    
    
    cv2.imshow("magic",frame)
    cv2.imshow("magic",f)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
    
    
cap.release()
cv2.destroyAllWindows()    
    
    


    
    
    
        
    