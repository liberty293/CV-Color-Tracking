import cv2
import numpy as np
import math

vid_capture = cv2.VideoCapture(0) #put in (0, *OPTIONAL* cv2.CAP_ANY) for webcam
 #from image sequence (where %04d means 4 digits like 0001 0002 etc.
#vid_capture = cv2.VideoCapture('Resources/Image_sequence/Cars%04d.jpg')
dispensing = True
minHSV = np.array([100,100,25])
maxHSV = np.array([125,225,225])
if (vid_capture.isOpened() == False):
    print("Error opening the video file")
# Read fps and frame count
else:
    # Get frame rate information
    # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
    fps = vid_capture.get(5) #foesnt work for webcam. all options at https://docs.opencv.org/4.x/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    print('Frames per second : ', fps,'FPS')
 
    # Get frame count
    # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
    frame_count = vid_capture.get(7)
    print('Frame count : ', frame_count)

max_center = (0,0)
sec_max_center = (0,0)
while(vid_capture.isOpened()):
  # vid_capture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
  ret, frame = vid_capture.read()
  if ret == True: #there is a frame to read
    #setting the instructions
    instruc = (50,100)
    instruc_end  = (instruc[0] + 1100, instruc[1] - 45)
    cv2.rectangle(frame, (instruc[0], instruc[1] +3), instruc_end, (255,255,255), thickness= -1, lineType=cv2.LINE_8)
    if (dispensing):
        cv2.putText(frame, "Press s to switch to aspirating", instruc, fontFace = cv2.FONT_HERSHEY_TRIPLEX, fontScale = 2, color = (0,0,0))
    else:
        cv2.putText(frame, "Press s to switch to dispensing", instruc, fontFace = cv2.FONT_HERSHEY_TRIPLEX, fontScale = 2, color = (0,0,0))
    
    #using the hsv color space (typically the best for color detection)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    maskHSV = cv2.inRange(hsv, minHSV, maxHSV) #make a mask for all colors in that range
    if(max_center != (0,0)):
        #make a circle around the previous two points
        mask_spacial = np.zeros(frame.shape[:2], dtype = "uint8")
        mask_spacial = cv2.circle(mask_spacial,max_center, 300,255,-1)
        mask_spacial = cv2.circle(mask_spacial,sec_max_center, 300,255,-1)
        mask = cv2.bitwise_and(maskHSV,mask_spacial)
        mask = maskHSV
    else:
        mask = maskHSV
    contours,_= cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #grab contours of mask
    if len(contours) > 1:
        #get max 2 contours
        max = float('-inf')
        second_last = float('-inf')

        max_contour = contours[0]
        sec_max_contour = contours[1]
        for contour in contours:
            if cv2.contourArea(contour)>max:
                sec_max_contour = max_contour
                max_contour = contour
                second_last = max
                max = cv2.contourArea(contour)
            elif cv2.contourArea(contour) > second_last:
                sec_max_contour = contour
                second_last = cv2.contourArea(contour)
        
        #get the center of each contour
        M=cv2.moments(max_contour)
        if(M['m00'] == 0):
            continue
        cx=int(M['m10']//M['m00'])
        cy=int(M['m01']//M['m00'])
        max_center = (cx,cy)

        cv2.circle(frame, (cx,cy),3,(0,0,255),-1)
        point_max = (cx, cy)
        M=cv2.moments(sec_max_contour)
        if(M['m00'] == 0):
            continue
        cx=int(M['m10']//M['m00'])
        cy=int(M['m01']//M['m00'])
        sec_max_center = (cx,cy)
        cv2.circle(frame, (cx,cy),3,(0,0,255),-1)
        point_sec = (cx, cy)

        #draw the contours
        cv2.drawContours(frame, max_contour, -1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.drawContours(frame, sec_max_contour, -1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.line(frame, point_max, point_sec, (255, 255, 0), thickness=1, lineType=cv2.LINE_AA) 

        text = "NA"
        #get the angles
        if((point_max[0]-point_sec[0]) != 0):
            angle = round(abs(math.atan((point_max[1]-point_sec[1])/(point_max[0]-point_sec[0]))*180/math.pi),2)
            text = str(angle)
        #org: Where you want to put the text
        org = (50,350)
        #highlight
        start_point =org
        end_point =(org[0] + 150, org[1] - 40)
        if dispensing == True:
            if (angle < 70 and angle > 45):
                color = (0,255,0)
            else:
                color = (0,0,255)
        else:
            if (angle > 85):
                color = (0,255,0)
            else:
                color = (0,0,255)

        # draw the rectangle
        cv2.rectangle(frame, start_point, end_point, color, thickness= -1, lineType=cv2.LINE_8)
        
        cv2.putText(frame, text, org, fontFace = cv2.FONT_HERSHEY_PLAIN, fontScale = 3, color = (0,0,0))
    cv2.imshow('Frame',frame)

    key = cv2.waitKey(50)
    if key == ord('s'):
        dispensing = not dispensing
    elif key == ord('q'):
      break
  else:
    break
 
# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()