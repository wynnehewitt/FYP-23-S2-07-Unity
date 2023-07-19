# FYP-23-S2-07-Unity
Repository for FYP files (Unity, OpenCV, etc)

Hallo Hallo, Instructions to how to run here.

https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/

Follow the steps up there.

OR 

PREREQUISITES
1. Python – 3.x

2. OpenCV – 4.5
Run “pip install opencv-python” to install OpenCV.

3. MediaPipe – 0.8.5
Run “pip install mediapipe” to install MediaPipe.

4. Tensorflow – 2.5.0
Run “pip install tensorflow” to install the tensorflow module.

5. Numpy – 1.19.3

You should have those 1 and 5 installed if you can compile python scripts

for 2, 3, 4: Run CMD.exe as administrator and type the commands there.

After installing everything u need, download

1) hand.py
2) ligma.unitypackage
3) In the link above, download the original file from there (hand-gesture-recognition-code) file

Replace TechVidvan-hand_gesture_detection.py with hand.py

To test if your webcam / detection works, open the folder where the hahand.py is located and type "cmd" into the address bar then hit enter
Your command prompt should open up and it will be in the same directory. Type "python hand.py" and hit enter. The setup takes awhile but your
webcam should launch and u can start testing out the various gestures that it can recognise. (Open gesture.names with notepad to see what is available)
Press "Q" while in the webcam window to quit.


Now open your unity and create a new project (Name and directory dont matter, jus make sure u know what and where it is). Drag and drop the HandGestureGame.unitypackage file into Unity Editor and it should auto extract and import. Now press the play button on top and with the webcam running, you should be able to change the middle cube which will determine the current tool the player is using. (Hammer = Red, Screwdriver = blue, Plier = Green)

Anything not clear jus ask me uwu
