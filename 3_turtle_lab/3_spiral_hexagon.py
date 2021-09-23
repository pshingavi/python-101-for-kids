import turtle

t = turtle.Turtle()
t.speed(0)
t.width(4)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for x in range(200):

    # Pick pen color
    t.pencolor(colors[x%7])

    # Move forward
    t.forward(x)

    # Turn left
    t.left(360/7)
