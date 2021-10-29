# THE ROCK, PAPER & SCISSORS GAME <img src="https://user-images.githubusercontent.com/65656071/126960759-5970a7e6-4995-4161-b7c0-f0dd74c802fb.png" width="60" height="60">

**DESCRIPTION:** The Rock paper scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). 

**AIM:** The project aims at designing a **Rock, Paper and Scissors Game** in which the two players will show their hand gestures on the screen and the computer will detect the gesture using **Image Processing and ML** and thereby declare the winner!    <img src="https://user-images.githubusercontent.com/65656071/126972741-ca6653e0-9c5e-4f7c-84cf-e3f0bc2d02ed.png" width="30" height="30">

**HOW IT WORKS:** 

<img src="https://user-images.githubusercontent.com/55792010/123235437-7d5b1b00-d4f9-11eb-97fc-1e4555b131a1.png">

1. A frame is displayed having subframes for recording the gestures of Player 1 and Player 2.

2. As soon as the space key is pressed, the gestures for Player 1 and 2 are recorded respectively.

3. By making contours and threshold images and further analysing them using convexity defects, the gesture is displayed on the main frame as Stone, Paper or Scissor.

4. Comparing the gestures of Player 1 and 2, the winner is  declared.

<img src="https://user-images.githubusercontent.com/65656071/126974445-1424d1e5-9c01-4abf-8f55-a2e3a7c5b475.png" width="400" height="300">

**DEMO:**

**TECHNOLOGIES USED:** 
- <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
- <img src="https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white"/>
- <img src="https://img.shields.io/badge/-MACHINE LEARNING-blue" height="24"/>
- <img src="https://img.shields.io/badge/-NUMPY LIBRARY-blue" height="24"/>

**FEATURES TO BE IMPLEMENTED IN FUTURE:**
1. Single Player vs Computer
2. Proper GUI for the Game

**REFERENCES:**
1. https://docs.opencv.org/4.5.2/d7/dbd/group__imgproc.html
2. https://www.youtube.com/watch?v=O62YO0zXioM&list=RDCMUCkQKVmPkp9Br6MNJYalsUGw&index=2

**CONTRIBUTORS:**
1. https://github.com/keshav2410garg <img src="https://img.shields.io/github/followers/keshav2410garg?label=Follow&style=social">
2. https://github.com/Prabhjot042001 <img src="https://img.shields.io/github/followers/Prabhjot042001?label=Follow&style=social">

**FILE DESCRIPTION:**

-***GAMEGUI.py***: The GUI to display instructions and how to play the game
- ***FINALGAME.py***: Game Model prepared using Image Recording and Processing approach. The Players show their respective gestures in the frame and the gestures are recorded in image format. Analysis is done on the recorded images and the winner is declared respectively. (The model is completed, GUI is being prepared for the same)


