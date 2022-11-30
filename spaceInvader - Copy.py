# importing turtle, math and random python modules
import turtle
import math
import random
import time
import json


json_scores = open('data.json')
scores_dict = json.load(json_scores)
json_scores.close()
# print(scores_dict)
# print(scores_dict['scores'])
sortedScores = dict(sorted(scores_dict['scores'].items(), key = lambda x:x[1], reverse = True))
scoreListString = ""
for k,v in sortedScores.items():
    print(v)
    scoreListString = scoreListString + "{0} : {1} \n".format(k,v)
print(scoreListString)



# Set up the game window screen
window = turtle.Screen()

begin_game = False
def begin(x,y): 
    global begin_game 
    begin_game = True
window.bgpic("start_game.gif") 
window.bgcolor("pink") 
window.title("Space Invaders - Math version")       
turtle.register_shape("beginner.gif")     
turtle.register_shape("advanced.gif") 
#create beginner turtle: 
turtle.register_shape("beginner.gif") 
beginner = turtle.Turtle() 
beginner.shape("beginner.gif") 
beginner.penup()
beginner.speed(0)
beginner.setposition(0,0) 


#create advanced turtle: 
turtle.register_shape("advanced.gif") 
advanced = turtle.Turtle() 
advanced.shape("advanced.gif") 
advanced.penup()
advanced.speed(0)
advanced.setposition(0,-70)
advanced.setheading(90)

# list of scores
highScore = turtle.Turtle()
highScore.speed(0)
highScore.color("red")
highScore.penup()
highScore.hideturtle()
highScore.setposition(-300, 260)
highScore.write(scoreListString, False, align="center", font=("Arial", 15, "normal"))

while True: 
    beginner.onclick(begin)
    advanced.onclick(begin)
    if begin_game:
        win = turtle.Screen()
        win.clear()
        break



while True:
    window.bgcolor("green")
    window.title("Space Invaders - CopyAssignment")
    window.bgpic("background.gif")

    # Register the shape
    #"C:\Users\yuyin\Downloads\CTD_1D\Picture1.png"
    turtle.register_shape("player.gif")
    turtle.register_shape("tick.gif")
    turtle.register_shape("cross.gif")
    turtle.register_shape("reset.gif")
    turtle.register_shape("end.gif") 
    turtle.register_shape("quit.gif")
    turtle.register_shape("endreset.gif")



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


    # def generate_qn_beginner():
    #     y = random.randint(0,9)
    #     total = random.randint(y,9)
    #     expected_ans = total - y 
    #     print("y value:",y,"total:",total,"expected:",expected_ans)

    #     equation = "x + {0} = {1}".format(y, total)
        
    #     return equation,expected_ans
    def generate_qn_beginner(): 
        qn_randomise = random.randint(1,4) 
        y = random.randint(0,9) 
        
        if qn_randomise == 1: #sum  
     
            total = random.randint(y,9) 
            expected_ans = total - y  
            print("y value:",y,"total:",total,"expected:",expected_ans) 
 
            equation = "a + {0} = {1}".format(y, total) 
             
            return equation,expected_ans 
             
        elif qn_randomise == 2: #minus  
            #y = random.randint(0,9) 
                positive_ans = False 
                while positive_ans == False: 
                    total = random.randint(0,y) 
                    expected_ans = total - y 
                    if expected_ans >= 0: 
                        positive_ans = True 
                 
                print("y value:", y, "total:",total,"expected:", expected_ans) 
                equation = "{0} - a = {1} ".format(total, y) 
                return equation,expected_ans 
         
        elif qn_randomise == 3: #times  
            nonzero = False 
            while nonzero == False: 
                total1 = random.randint(0,9) 
                total = total1*y 
                if total != 0: 
                    nonzero = True  
 
            expected_ans = total1 
            print("y value:", y, "total:",total,"expected:", expected_ans) 
            equation = "a x  {0} = {1}".format(y, total) 
            return equation,expected_ans 
         
        else: 
            nonzero = False 
            while nonzero == False: 
                total1 = random.randint(0,9) 
                total = total1*y 
                if total != 0: 
                    nonzero = True  
 
            expected_ans = total1 
            print("y value:", y, "total:",total,"expected:", expected_ans) 
            equation = "{1} / a = {0}".format(y, total) 
            return equation,expected_ans
    eqns = {}
    for num in range(10):
        while True:
            eqn,ans = generate_qn_beginner()
            if eqn in eqns:
                continue
            else:
                break
        eqns[eqn] = ans

    # new!! - write equation at the center of the frame
    print(list(eqns.keys()))
    qn_num = 0
    print(qn_num)
    eqn_pen = turtle.Turtle()
    eqn_pen.speed(0)
    eqn_pen.color("white")
    eqn_pen.penup()
    eqn_pen.setposition(200, 270)
    def write_qn(qn_num):
        if qn_num<10:
            eqn_pen.clear()
            eqn_pen.write(
                list(eqns.keys())[qn_num], False, align="center", font=("Arial", 14, "normal"), 
            )
            eqn_pen.hideturtle()
        else:
            eqn_pen.clear()
    write_qn(qn_num)

    # ============[ end of function]=================









    # Create the player turtle
    player = turtle.Turtle()
    player.shape("player.gif")
    player.penup()
    player.speed(0)
    player.setposition(0, -250)
    player.setheading(90)
    playerspeed = 15
    #create tick turtle
    tick = turtle.Turtle()
    tick.shape("tick.gif")
    tick.penup()
    # tick.setheading(90)
    tick.speed(0)
    tick.hideturtle()
    #create cross turtle
    cross = turtle.Turtle()
    cross.shape("cross.gif")
    cross.penup()
    # cross.setheading(90)
    cross.speed(0)
    cross.hideturtle()
    #create reset turtle:
    reset = turtle.Turtle()
    reset.shape("reset.gif")
    reset.penup()
    # reset.setheading(90)
    reset.speed(0)
    reset.setposition(-330, 310)
    # create quit turtle
    quit = turtle.Turtle()
    quit.hideturtle()
    quit.shape("quit.gif")
    quit.penup()
    # quit set position (0,0)
    quit.speed(0)
    quit.setposition(0,0)
    quit.hideturtle()
    # Choose a number of enemies
    number_of_enemies = 10
    # Creat an empty list of enemies
    ordered_enemies = {}
    #choose pos of ans:
    ans_pos = random.randint(0,9)
    # Add enemies to the list
    for eqn,ans in eqns.items():
        # create the enemy
        ordered_enemies[turtle.Turtle()] = ans
    enemies_list = list(ordered_enemies.items())
    random.shuffle(enemies_list)
    enemies = dict(enemies_list)

    # end state 
        # win game state - create this function and define conditions that happen at this state 
        # hide turtles - follow game over
        # show reset turtle 
        # create restart and quit button -> register shape for individual gifs
        # onclick conditions for both 
        # define proper win state as the condition for when to call function 
    def game_pass(): 
        player.hideturtle()
        bullet.hideturtle()
        for e in enemies:
            e.hideturtle()
        window.bgpic("end.gif") # insert relevant game pass image
        window.bgcolor("black")
        reset.showturtle()
        reset.setposition(-100, -150)
        reset.shape("endreset.gif")
        quit.showturtle()
        quit.setposition(100, -150)
        eqn_pen.clear()
        score_pen.clear()
        score_pen.setposition(0, 150)
        scorestring = "SCORE: %s" % score
        score_pen.write(scorestring, False, align="center", font=("Arial", 50, "bold"))

    def quit_game(x,y):
        turtle.bye()
    
    
    
        
    phase = 0
    for enemy,digit in enemies.items():
        enemy.color("Red")
        num = "digits/" + str(digit)+ ".gif"
        turtle.register_shape(num)
        enemy.shape(num)
        enemy.penup()
        enemy.speed(0)
        x = random.randint(-200+(phase*50),-185+(phase*50) )
        y = random.randint(100, 250)
        enemy.setposition(x, y)
        phase = phase+1

    enemyspeed = 5

    # Creat the player's bullet
    bullet = turtle.Turtle()
    bullet.color("white")
    bullet.shape("triangle")
    bullet.penup()
    bullet.speed(5)
    bullet.setheading(90)
    bullet.shapesize(0.5, 0.5)
    bullet.hideturtle()
    bullet.setposition(0, -400)
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
            

    #takes in enemy at bullet path then checks with answer
    def collision(enemy):
        global qn_num
        global score
        global Game_Over
        global bulletstate
        if enemy.isvisible():
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            # x = random.randint(-200, 200)
            # y = random.randint(100, 250)
            # enemy.setposition(x, y)
            # enemyspeed += 0.5
            # update the score
            
            if enemies[enemy] == list(eqns.values())[qn_num]:
                enemy.hideturtle()
                tick.setpos(enemy.xcor(),enemy.ycor())
                tick.showturtle()
                time.sleep(0.3)
                tick.hideturtle()
                # enemy.setpos(-300,300)
                score += 10
                scorestring = "Score: %s" % score
                #score_equation = "X + 2 = 4"
                score_pen.clear()
                score_pen.write(
                    scorestring, False, align="left", font=("Arial", 14, "normal"), 
                )
                qn_num+=1
                write_qn(qn_num)
                Game_Over = True
            else:
                enemy.hideturtle()
                cross.setpos(enemy.xcor(),enemy.ycor())
                cross.showturtle()
                time.sleep(0.3)
                cross.hideturtle()
                enemy.setpos(enemy.xcor(),enemy.ycor())
                enemy.showturtle()
                score -= 5
                scorestring = "Score: %s" % score
                #score_equation = "X + 2 = 4"
                score_pen.clear()
                score_pen.write(
                    scorestring, False, align="left", font=("Arial", 14, "normal"), 
                )

    # For collision between enemy and player
    def isCollision_enemy_player(t1, t2):
        if type(t1) == 'int':
            pass
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
    rst = False
    while True:
        def startover(x,y):
            global rst
            rst = True
        reset.onclick(startover)
        quit.onclick(quit_game)
        for enemy,digit in enemies.items():
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
                
            # check for a collision between the player and enemy
            if isCollision_enemy_player(player, enemy):
                Game_Over = True
            if qn_num == 10:
                Game_Over = True
            if Game_Over == True:
                qn_num = 0
                game_pass()

        # Move the bullet with turtle.forward when it theres
        if bulletstate == "fire":
            enemy_pos = 0
            xbull = bullet.xcor()
            # print(bullet.ycor())
            # newEnem = {i.ycor():i for i in enemies}
            # sortEnem = {ycor:Enem for ycor,Enem in sorted(newEnem.items())}
            # print(sortEnem)git 
            for enemy,ans in enemies.items():
                if enemy.isvisible():
                    xcoord = enemy.xcor()
                    # print(xcoord)
                    if math.isclose(xbull,xcoord,rel_tol=0.15,abs_tol=15):
                        bullet.goto(xbull,enemy.ycor())
                        # print(enemy.ycor())
                        # print(enemy.xcor())
                        enemy_pos+=1
                        bullet.hideturtle()
                        bulletstate = "ready"
                        #colliion func
                        collision(enemy)
                        break
            if enemy_pos == 0:
                bullet.forward(530)
                bullet.hideturtle()
                bulletstate = "ready"
                    
            # y += bulletspeed
            # bullet.sety(y)
            # bullet.forward(600)

        # Check to see if the bullet has gone to the top
        if bullet.ycor() > 275:
            bullet.hideturtle()
            bulletstate = "ready"
        if rst:
            # for enemy,digits in enemies.items():
            #     enemy.clear()
            # player.clear()
            # bullet.clear()
            # break
            win = turtle.Screen()
            win.clear()
            break

# turtle.done()