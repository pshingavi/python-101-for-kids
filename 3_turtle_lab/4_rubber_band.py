# Draw square spiral

# Draw x pixels long line, turn 90 degree

import turtle

t = turtle.Pen()    # Get turtle Pen
turtle.bgcolor('black') # Change background color
t.speed(0)  # Draw fast

sides = 6
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides + x)
    t.left(360/sides + 91)
    t.width(x*sides/200)
