# CTD 1D Group E Math Invaders
# Table of Contents
1. [Members](#members)
2. [Overview](#overview)
3. [Game Description](#overview)
4. [Documentation](#documentation)
    1. [Libraries](#libraries)
    2. [Directory Structure](#directory-structure)
    3. [Game Music](#game-music)
    4. [Functions](#functions)
        1. [start_game.py](#start_pagepy)
        2. [equations.py](#equationspy)
        3. [game_bg.py](#game_bgpy)
        4. [game_icons.py](#game_iconspy)
    5. [main.py](#mainpy)
<br/>
<br/>
## Members
- Gangesh Kumar
- Haresh Jayant 
- Julian How
- Yu Ying
- Sushmitha

## Overview

Inspired by the Japanese shooting game space invaders, where the player shoots the aliens that are falling from space, we recreated it into a math version of space invaders. We incorporated math by adding a math equation and replacing the aliens with numbers which are answers to the equations. 

## Game Desciprtion
xxx

## To run:
install public-pixel-font

```bash
python3 main.py
```

## Documentation

### Libraries
```python
import turtle
import math
import random
import time
import json
from itertools import cycle
import sys 
import subprocess
from threading import Thread
```
### Directory Structure
```bash
├── data.json
├── digits
├── functions
│   ├── equations.py
│   ├── game_bg.py
│   ├── game_icons.py
│   ├── jsonfunc.py
│   └── start_page.py
├── game_gifs
├── game_music
├── main.py
└── public-pixel-font
```
* data.json contains the respective user name and their scores
* digits contains the images 0-99 which will be used as 'enemies' in the game 
* functions is a folder containing the following python files with the various functions that will be called in main.py
    ```python
    #imports function used to send and get data from json file
    from functions import jsonfunc.py
    #imports function to setup startpage
    from functions import start_page.py
    #function to create equations for beginner/advanced mode
    from functions import equations.py
    #imports functions related to background of game
    from functions import game_bg.py
    #imports functions related to icons used in game eg. player
    from functions import game_icons.py

## Game Music
All background music in this code is played using thread and subprocess with the following syntax
```python
if sys.platform == 'linux2': 
        bgmusic = subprocess.Popen(["afplay","<soundfile>"])
    elif sys.platform == 'darwin': 
        bgmusic = subprocess.Popen(["afplay","<soundfile>"])
```
The above code is then attached to a thread using a function to allow for it to be run concurrently with the game.
## Functions
xx
<br/>
### jsonfunc.py
```python
#returns sorted scores for advanced and beginner mode to display on startpage
startpagescrs()
#takes in player name and score and stores it in data.json
endpagescr(nameInput,game_mode,score)
```



### start_page.py
```python
#Takes in sorted scores and displays top 5 for each mode on the start screen of game followed by respective icons. together with start page background and icons as turtle objects. Background music for start screen is played here
start_page(beginnerScores,advScores)
```

### equations.py
```python 
#generates beginner level questions eg. a + 9 = 13
generate_qn_beginner()
#generates advanced level questions eg. a x 93 = 4836
generate_qn_advanced()
```

### game_bg.py
```python
#sets up all game icons and 'enemies'(digits)
bg_setup()
#clears/hides background icons
bg_end()
#closes turtle window
quit_game()
#takes in qn num and eqns dictionary andwrites qn onto turtle screen
write_qn(qn_num,eqns)
```
### game_icons.py
```python
#setup player,bullet,tick,cross,reset,quit icons
icons_setup()
#hiding icons when game is over
icons_end()
#for bullet to appear and give a sound effect
fire_bullet()
```

## main.py
xx

