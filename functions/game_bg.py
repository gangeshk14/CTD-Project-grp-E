import turtle
import random



score = 0
qn_num = 0
def write_qn(qn_num,eqns):
    if qn_num<10:
        eqn_pen.clear()
        eqn_pen.write(
            list(eqns.keys())[qn_num], False, align="center", font=("Arial", 14, "normal"), 
        )
        eqn_pen.hideturtle()
    else:
        eqn_pen.clear()

def bg_setup():
    global border_pen,score_pen, eqn_pen, end_message
    border_pen = turtle.Turtle()
    score_pen = turtle.Turtle()
    eqn_pen = turtle.Turtle()
    end_message = turtle.Turtle()
    # Register the shape
    #"C:\Users\yuyin\Downloads\CTD_1D\Picture1.png"
    turtle.register_shape("game_gifs/player.gif")
    turtle.register_shape("game_gifs/tick.gif")
    turtle.register_shape("game_gifs/cross.gif")
    turtle.register_shape("game_gifs/reset.gif")
    turtle.register_shape("game_gifs/end.gif") 
    turtle.register_shape("game_gifs/quit.gif")
    turtle.register_shape("game_gifs/endreset.gif")



    # Draw border
    border_pen.speed(0)
    border_pen.color("white")
    border_pen.penup()
    border_pen.setposition(-300, -300)
    border_pen.pendown()
    border_pen.pensize(3)
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
    border_pen.hideturtle()


    # Set the score to 0
    global score

    # Draw the pen
    score_pen.speed(0)
    score_pen.color("red")
    score_pen.penup()
    score_pen.setposition(-290, 270)
    scorestring = "SCORE: %s" % score
    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
    score_pen.hideturtle()

    eqn_pen.speed(0)
    eqn_pen.color("white")
    eqn_pen.penup()
    eqn_pen.setposition(200, 270)

    end_message.speed(0)
    end_message.color("red") 
    end_message.penup()
    end_message.setposition(0,200) 
    end_message.hideturtle()

    return border_pen, score_pen, eqn_pen, end_message

def bg_end(scorestring):
        eqn_pen.clear()
        score_pen.clear()
        score_pen.setposition(0, 150)
        score_pen.write(scorestring, False, align="center", font=("Arial", 40, "bold"))
        if (score < 70):
            end_message.write("You need to be better", align="center", font=("Arial", 40, "bold"))
        else:
            end_message.write("Good enough", align="center", font=("Arial", 40, "bold"))

def quit_game(x,y):
    turtle.bye()