# TechVidvan hand Gesture Recognizer

# import necessary packages

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

import math
import socket
import time

# stuff needed to import data to unity
UDP_IP = "127.0.0.1"
UDP_PORT = 5065

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

counter = 0    #int counter to track 1 action

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)


# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    # print(result)
    
    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            # print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]

    # show the prediction on the frame
    cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0,0,255), 2, cv2.LINE_AA)

    cv2.namedWindow("Output", cv2.WINDOW_NORMAL)

    cv2.resizeWindow("Output", 280, 190)

    # Show the final output
    cv2.imshow("Output", frame) 
    
    # if the player makes a certain gesture, do a certain action
    if(className == "fist" and counter == 0):
        sock.sendto( ("Hammer").encode(), (UDP_IP, UDP_PORT) )
        print("_"*10, "Hammer selected!", "_"*10)
        counter += 1
           
    if(className == "thumbs down" and counter == 0):
        sock.sendto( ("Screwdriver").encode(), (UDP_IP, UDP_PORT) )
        print("_"*10, "Screwdriver selected!", "_"*10)
        counter += 1       
            
    if(className == "peace" and counter == 0):
        sock.sendto( ("Nailgun").encode(), (UDP_IP, UDP_PORT) )
        print("_"*10, "Nailgun selected!", "_"*10)
        counter += 1

    if(className == "okay" and counter == 0):
        sock.sendto( ("okay").encode(), (UDP_IP, UDP_PORT) )
        print("_"*10, "Tool used!", "_"*10)
        counter += 1
            
    if(className == "thumbs up" and counter == 0):
        sock.sendto( ("thumbs up").encode(), (UDP_IP, UDP_PORT) )
        print("_"*10, "Repair completed!", "_"*10)
        counter += 1
            
    # this is to ensure everytime the player makes a gesture, it only takes in once
    if((className == "stop" or className == "live long") and counter != 0):
        counter = 0
            
    
    # exit program
    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()

cv2.destroyAllWindows()