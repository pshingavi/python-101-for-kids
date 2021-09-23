# draws an interactive Christmas tree, click to add names!
from turtle import *
import random
colormode(255) # remove this line if running on Trinket.io 
students = ["Bo G.", "Bo A.", "Charlie", "Savannah", "Kristin", "Nancy Belle", "Emily", "Severen", "Thomas", "Taven", "Ethan", "Jack", "Alex"]
random.shuffle(students)
snum = 0
shape("turtle")
color("brown")
penup()
goto(-20, -175)
pendown()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
color("green")
penup()
goto(-150,-135)
pendown()
forward(300)
left(120)
forward(300)
left(120)
forward(300)
color("gold")
penup()
right(180)
forward(300)
pendown()
dot(60)
def draw_name(x,y):
  global snum
  rc = students[snum % len(students)]
  snum = snum+1
  r = random.randint(0,256)
  g = random.randint(0,256)
  b = random.randint(0,256)
  colormode(255)
  color((r, g, b))
  penup()
  goto(x,y)
  pendown()
  dot(20)
  penup()
  forward(8)
  pendown()
  write(rc, font=("Arial", 12, "normal"))
  penup()
  goto(0,110)
  color("gold")
getscreen().onscreenclick(draw_name)