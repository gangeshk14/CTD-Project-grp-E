# from PIL import Image, ImageDraw, ImageFont
# import os

# def text_on_img(filename, text):
    
#     "Draw a text on an Image, saves it, show it"
#     fnt = font = ImageFont.truetype("Arial.ttf", 20)

#     # create image
#     image = Image.new(mode = "RGB", size = (30,30), color = "black")
#     draw = ImageDraw.Draw(image)
    
#     # draw text
#     draw.text((5,10), text, font=fnt, fill=(255,255,255))
    
#     # save file
#     image.save(filename)
    
#     # show file
# for x in range(0,99):
#     filename = 'digits/' + str(x) + '.gif'
#     text = str(x)
#     text_on_img(filename,text)

# import math
# import random
# if math.isclose(0,-1,rel_tol=0.25,abs_tol=25):
#     print('x')
# dic = {1:'hi', 3: 'grefds', 2:'frds'}
# # dic.sort()
# ls = list(dic.items())
# print(dict(ls))
# random.shuffle(ls)
# print(dict(ls))

# sdic = {x:y for x,y in random.shuffle(dic.items())}
# # print(sdic)

# from turtle import *

# import turtle as tur 
  

# def func(i,j):
#     tur.right(90)
#     tur.forward(100)
#     print('xxxxx')
  
# tur.speed(1)
  
# tur.forward(100)
 
# tur.onclick(func)
# rst = 3
# def startover():
#     global rst
#     rst +=1
#     print(rst)
# startover()
import sys 
import subprocess 
from threading import Thread
import time
# def playmusic():
#     if sys.platform == 'linux2': 
#         call(["xdg-open","sound.mp3"]) 
#     elif sys.platform == 'darwin': 
#         call(["afplay","sound.mp3"])

process = subprocess.Popen(["afplay","shrek.m4a"])
time.sleep(5)
process.terminate()


