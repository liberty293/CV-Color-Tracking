# CV Color Tracking
 Color Tracking to for pipet angle detection.
 
 The computer executable is located in te dist folder.
 
 For user: place painters tape around the top and bottom of the tape. Turn on the application, ensuring the pipette is in front of the camera. 
 The application will then report the angle of the pipette, turning green if the angle is correct.
 
 To switch between detection of the aspirating vs dispensing angle, press s.
 To end the application, press q
 
 For developers
 The applciation was used to detect the color of painters tape. To detect other colors, place color examples in the Blues folder and run color thresholds.
 The file plots the color distributions for each colorspace as well as output the minimum and maximum color values. From there, you can choose the color space with the narrowest band and edit the main.py file with the correct colors. Note it may be valuable to choose thresholds that encompass the majority of the color in the graph rather than max and minimum numbers outputted if you are getting large artifacts.
