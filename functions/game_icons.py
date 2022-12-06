import turtle
import sys 
import subprocess
from threading import Thread
#setup turtles
def shootsoundeff():
        global shootsound
        if sys.platform == 'linux2': 
            call(["xdg-open","sound.mp3"]) 
        elif sys.platform == 'darwin': 
            shootsound = subprocess.Popen(["afplay","game_music/shoot.wav"])
def icons_setup():
    global player, tick, reset, quit, cross, bullet
    player = turtle.Turtle()
    tick = turtle.Turtle()
    cross = turtle.Turtle()
    reset = turtle.Turtle()
    quit = turtle.Turtle()
    bullet = turtle.Turtle()
      # Create the player turtle
    player.shape("game_gifs/player.gif")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    # player.setheading(90)
    #create tick turtle
    tick.shape("game_gifs/tick.gif")
    tick.penup()
    # tick.setheading(90)
    tick.speed(0)
    tick.hideturtle()
    #create cross turtle
    cross.shape("game_gifs/cross.gif")
    cross.penup()
    # cross.setheading(90)
    cross.speed(0)
    cross.hideturtle()
    #create reset turtle:
    reset.shape("game_gifs/reset.gif")
    reset.penup()
    # reset.setheading(90)
    reset.speed(0)
    reset.setposition(-330, 310)
    # create quit turtle
    quit.hideturtle()
    quit.shape("game_gifs/quit.gif")
    quit.penup()
    # quit set position (0,0)
    quit.speed(0)
    quit.setposition(0,0)
    quit.hideturtle()
    bullet.color("white")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(5)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()
    bullet.setposition(0, -400)
    return player,tick,cross,reset,quit,bullet
#end game
def icons_end():
    player.hideturtle()
    reset.shape("game_gifs/endreset.gif")
    reset.setposition(-100, -150)
    quit.showturtle()
    quit.setposition(100, -150)

#game methods
playerspeed = 30
def plyr_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def plyr_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


bulletstate = "ready"

def fire_bullet():
    # Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()
        shootmusic = Thread(target=shootsoundeff)
        shootmusic.start()