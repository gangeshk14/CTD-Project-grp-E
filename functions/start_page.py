import turtle
from itertools import cycle
import sys 
import subprocess
from threading import Thread

def openstartmusic():
    global startmusic
    if sys.platform == 'linux2': 
        call(["xdg-open","sound.mp3"]) 
    elif sys.platform == 'darwin': 
        startmusic = subprocess.Popen(["afplay","game_music/start_game.wav"])

def start_page(beginnerScores,advScores):
    global startplay
    startplay = Thread(target=openstartmusic)
    startplay.start()
    startgame = turtle.Turtle()
    beginner = turtle.Turtle()
    advanced = turtle.Turtle() 
    clickbtn = turtle.Turtle()
    window = turtle.Screen()
    canvas = turtle.getcanvas()
    window.bgpic("game_gifs/start_game.gif") 
    window.bgcolor("pink") 
    window.title("Space Invaders - Math version")       
    turtle.register_shape("game_gifs/beginner.gif")     
    turtle.register_shape("game_gifs/advanced.gif") 
    turtle.register_shape("game_gifs/black.gif") 
    #create beginner turtle: 
    turtle.register_shape("game_gifs/beginner.gif") 
    startgame.penup()
    startgame.speed(0)
    startgame.hideturtle()
    startgame.color('white')
    startgame.setposition(-160,100)
    startgame.write('Ready?', False, align="left", font=("Public Pixel", 60, "bold"))
    beginner.shape("game_gifs/beginner.gif") 
    beginner.penup()
    beginner.speed(0)
    beginner.setposition(-110,0) 
    # beginnertxt = turtle.Turtle() 
    # beginnertxt.color('white')
    # beginnertxt.penup()
    # beginnertxt.speed(0)
    # beginnertxt.setposition(-144,-3) 
    # beginnertxt.hideturtle()
    # beginnertxt.write('BEGINNER', False, align="left", font=("Public Pixel", 11, "bold"))

    #create advanced turtle: 
    turtle.register_shape("game_gifs/advanced.gif") 
    advanced.shape("game_gifs/advanced.gif") 
    advanced.penup()
    advanced.speed(0)
    advanced.setposition(70,0)
    advanced.setheading(90)

    # list of beginner scores
    rank = 1
    bgHighScore = turtle.Turtle()
    bgHighScore.speed(0)
    # bgHighScore.color("#FF5733")
    bgHighScore.color("white")
    bgHighScore.penup()
    bgHighScore.hideturtle()
    bgHighScore.setposition(-145, -50)
    if len(beginnerScores)<5:
        scorerange = len(beginnerScores)
    else:
        scorerange = 5
    for pos in range(scorerange):
        k,v = list(beginnerScores.items())[pos]
        output = str(rank) + '. ' + k + ': ' +str(v)
        if sys.platform == 'darwin':
            bgHighScore.write(output, False, align="left", font=("Public Pixel", 9, "bold"))
            bgHighScore.goto(-145, bgHighScore.ycor() - 20)
            rank = rank + 1
        else:
            bgHighScore.write(output, False, align="left", font=("Public Pixel", 8, "bold"))
            bgHighScore.goto(-145, bgHighScore.ycor() - 20)
            rank = rank + 1


    # list of advancedscores
    advHighScore = turtle.Turtle()
    advHighScore.speed(0)
    advHighScore.color("#FF5733")
    advHighScore.penup()
    advHighScore.hideturtle()
    advHighScore.setposition(30, -50)
    rank = 1
    if len(advScores)<5:
        scorerange = len(beginnerScores)
    else:
        scorerange = 5
    for pos in range(scorerange):
        k,v = list(advScores.items())[pos]
        output = str(rank) + '. ' + k + ': ' +str(v)
        advHighScore.write(output, False, align="left", font=("Public Pixel", 9, "bold"))
        advHighScore.goto(30, advHighScore.ycor() - 20)
        rank +=1

    clickbtn.color('white')
    clickbtn.speed(0)
    clickbtn.penup()
    clickbtn.hideturtle()
    clickbtn.setpos(-170,50)
    return startgame, beginner,advanced, clickbtn, window, canvas
    