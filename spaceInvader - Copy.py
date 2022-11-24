# importing turtle, math and random python modules
import turtle
import math
import random

# Set up the game window screen
window = turtle.Screen()
window.bgcolor("green")
window.title("Space Invaders - CopyAssignment")
window.bgpic("background.gif")

# Register the shape
#"C:\Users\yuyin\Downloads\CTD_1D\Picture1.png"
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


# Draw border
border_pen = turtle.Turtle()
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
score = 0

# Draw the pen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("red")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "SCORE: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# ===================================
# new!!
# 1 - create function to generate equations 
# ==> x(expected ans) + y = total[num smaller than 10]
# 2 - create pictures of aliens with numbers? 1-9 [beginner] -- manually 
# 3 - store the pictures with id in a dict or list 


# generate random equation 
# 1) add + - / * eqns 
# 2) change invader gif to numbers 
# 3) allow users to spam bullets? 
# 4) if user hits the wrong value ==> minus mark or minus life 


def generate_qn_beginner():
    y = random.randint(0,9)
    total = random.randint(y,9)
    expected_ans = total - y 
    print("y value:",y,"total:",total,"expected:",expected_ans)

    equation = "x + {0} = {1}".format(y, total)
    
    return equation

print(generate_qn_beginner())

# new!! - write equation at the center of the frame
eqn_pen = turtle.Turtle()
eqn_pen.speed(0)
eqn_pen.color("white")
eqn_pen.penup()
eqn_pen.setposition(200, 270)
eqn_string = generate_qn_beginner()

eqn_pen.write(
    eqn_string, False, align="center", font=("Arial", 14, "normal"), 
)
eqn_pen.hideturtle()

# ============[ end of function]=================









# Create the player turtle
player = turtle.Turtle()
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

# Choose a number of enemies
number_of_enemies = 10
# Creat an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    # enemy.color("Red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 5

# Creat the player's bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 30

# define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"



# Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


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


# For collision between enemy and bullet
def isCollision_enemy_bullet(t1, t2):
    distance = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    if distance < 25:
        return True
    else:
        return False


# For collision between enemy and player
def isCollision_enemy_player(t1, t2):
    distance = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2)
    )
    if distance < 30:
        return True
    else:
        return False


# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
Game_Over = False
missed_enemies = 0
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 270:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
                    missed_enemies += 1
                    if missed_enemies == 5:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
            # Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -270:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285 and Game_Over == False:
                    e.hideturtle()
                    missed_enemies += 1
                    if missed_enemies == 5:
                        Game_Over = True
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.setposition(x, y)
                    e.showturtle()
            # Change enemy direction
            enemyspeed *= -1

        # check for a collision between the bullet and the enemy
        if isCollision_enemy_bullet(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            enemyspeed += 0.5
            # update the score
            score += 10
            scorestring = "Score: %s" % score
            #score_equation = "X + 2 = 4"
            score_pen.clear()
            score_pen.write(
                scorestring, False, align="left", font=("Arial", 14, "normal"), 
            )
            
        # check for a collision between the player and enemy
        if isCollision_enemy_player(player, enemy):
            Game_Over = True
        if Game_Over == True:
            player.hideturtle()
            bullet.hideturtle()
            for e in enemies:
                e.hideturtle()
            window.bgpic("end.gif")
            break

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

turtle.done()