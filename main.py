from functions import jsonfunc, start_page, game_bg, equations, game_icons
# importing turtle, math and random python modules
import turtle
import math
import random
import time
import json
from itertools import cycle
import sys 
import subprocess
from threading import Thread

try:
    while True:
        window = turtle.Screen()

        #get high scores
        beginnerScores, advScores = jsonfunc.startpagescrs()

        begin_game = False
        nameInput = ""

        def tickcolli():
            global ticksound
            if sys.platform == 'linux2': 
                call(["xdg-open","game_music/correct.mp3"]) 
            elif sys.platform == 'darwin': 
                ticksound = subprocess.Popen(["afplay","game_music/correct.mp3"])
        def crosscolli():
            global xsound
            if sys.platform == 'linux2': 
                call(["xdg-open","game_music/wrong.mp3"]) 
            elif sys.platform == 'darwin': 
                xsound = subprocess.Popen(["afplay","game_music/wrong.mp3"])

        # bgmusic = Thread(target=playbg)
        tickmusic = Thread(target=tickcolli)
        crossmusic = Thread(target=crosscolli)
        def beginner_begin(x,y):
            global game_mode
            game_mode = "beginner"
            global nameInput
            nameInput= turtle.textinput("Please input a username", "Please input a username")
            global begin_game 

            while nameInput.strip() == "" or len(nameInput) >10 :
                if nameInput.strip() == "":
                    nameInput = turtle.textinput("You MUST input a valid name", "You MUST input a valid name")
                elif len(nameInput) >10:
                    nameInput = turtle.textinput("Name is too long", "Name must be less than 10 characters")
                elif nameInput == None:
                    begin_game = False

            begin_game = True 

        def advanced_begin(x,y):
            global game_mode
            game_mode = "advanced"
            print(game_mode)
            global nameInput
            nameInput= turtle.textinput("Please input a username", "Please input a username")
            global begin_game 

            while nameInput == "" or len(nameInput) >10 :
                if nameInput == "":
                    nameInput = turtle.textinput("You MUST input a valid name", "You MUST input a valid name")
                elif len(nameInput) >10:
                    nameInput = turtle.textinput("Name is too long", "Name must be less than 10 characters")
            
                elif nameInput == None:
                    begin_game = False

            begin_game = True 


        # Set up the game window screen
        startgame, beginner,advanced, clickbtn, window, canvas = start_page.start_page(beginnerScores,advScores)

        colors = ['red','green','blue']
        itercolors = cycle(colors)


        while True: 
            clickbtn.write('Click buttons below to begin', False, align="left", font=("Public Pixel", 13, "bold"))
            clickbtn.color(next(itercolors))
            beginner.onclick(beginner_begin)
            advanced.onclick(advanced_begin)
            if begin_game:
                win = turtle.Screen()
                win.clear()
                start_page.startmusic.terminate()
                break

        print(game_mode)
        while True:
            #setup background
            window.bgcolor("black")
            window.bgpic("game_gifs/background.gif")
            border_pen, score_pen, eqn_pen, end_message = game_bg.bg_setup()
            score = game_bg.score
            print('rest')

            #generate dic with eqn,ans as key,value pair
            eqns = {}
            for num in range(10):
                while True:
                    if game_mode == "beginner":
                        eqn,ans = equations.generate_qn_beginner()
                    elif game_mode == "advanced":
                        eqn,ans = equations.generate_qn_advanced()
                    if eqn in eqns:
                        continue
                    else:
                        break
                eqns[eqn] = ans

            # new!! - write equation at the center of the frame
            # print(list(eqns.keys()))
            qn_num = game_bg.qn_num
            #write 1st qn
            game_bg.write_qn(qn_num,eqns)
            #initialize all game icons
            player,tick,cross,reset,quit,bullet = game_icons.icons_setup()
            playerspeed = 10
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


            def game_pass(): 
                bullet.hideturtle()
                for e in enemies:
                    e.hideturtle()
                if score == 100:
                    window.bgpic("game_gifs/win.gif") # insert relevant game pass image
                else:
                    window.bgpic("game_gifs/end.gif")
                window.bgcolor("black")
                game_icons.icons_end()
                scorestring = "SCORE: %s" % score
                game_bg.bg_end(scorestring, score,game_mode,beginnerScores,advScores)
                jsonfunc.endpagescr(nameInput,game_mode,score)        

            #takes in enemy at bullet path then checks with answer
            def collision_enemy_bullet(enemy):
                global qn_num
                global score
                global Game_Over
                global tickmusic
                global crossmusic
                if enemy.isvisible():
                    # Reset the bullet
                    bullet.hideturtle()
                    game_icons.bulletstate = "ready"
                    bullet.setposition(0, -400)
                    if enemies[enemy] == list(eqns.values())[qn_num]:
                        tickmusic.start()
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
                        game_bg.write_qn(qn_num,eqns)
                        tickmusic = Thread(target=tickcolli)
                        # Game_Over = True
                    else:
                        crossmusic.start()
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
                        crossmusic = Thread(target=crosscolli)

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
            turtle.onkey(game_icons.plyr_left, "Left")
            turtle.onkey(game_icons.plyr_right, "Right")
            turtle.onkey(game_icons.fire_bullet, "space")
            # Main game loop
            Game_Over = False
            rst = False
            while True:
                def startover(x,y):
                    global rst
                    rst = True
                reset.onclick(startover)
                quit.onclick(game_bg.quit_game)
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
                        # Change enemy direction
                        enemyspeed *= -1

                    if enemy.xcor() < -270:
                        # Move all enemies down
                        for e in enemies:
                            y = e.ycor()
                            y -= 40
                            e.sety(y)
                        # Change enemy direction
                        enemyspeed *= -1
                        
                    # check for a collision between the player and enemy
                    if isCollision_enemy_player(player, enemy):
                        Game_Over = True
                    if qn_num == 10:
                        Game_Over = True
                if Game_Over == True:
                    game_pass()


                # Move the bullet with turtle.forward when it theres
                if game_icons.bulletstate == "fire":
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
                                game_icons.bulletstate = "ready"
                                #colliion func
                                collision_enemy_bullet(enemy)
                                break
                    if enemy_pos == 0:
                        bullet.forward(530)
                        bullet.hideturtle()
                        game_icons.bulletstate = "ready"
                            
                    # y += bulletspeed
                    # bullet.sety(y)
                    # bullet.forward(600)

                # Check to see if the bullet has gone to the top
                if bullet.ycor() > 275:
                    bullet.hideturtle()
                    game_icons.bulletstate = "ready"
                if rst:
                    # for enemy,digits in enemies.items():
                    #     enemy.clear()
                    # player.clear()
                    # bullet.clear()
                    # break
                    win = turtle.Screen()
                    win.clear()
                    game_bg.bgmusic.terminate()
                    break
            if rst and Game_Over:
                win = turtle.Screen()
                win.clear()
                game_bg.bgmusic.terminate()
                break
except:
    if hasattr(start_page, 'startmusic'):
        start_page.startmusic.terminate()
    if hasattr(game_bg, 'bgmusic'):
        game_bg.bgmusic.terminate()
