# Draw square spiral

# Draw x pixels long line, turn 90 degree

import turtle

# Get turtle Pen
t = turtle.Pen()

# Draw fast
t.speed(0)

for x in range(100):
    t.forward(x)
    #t.forward(2*x)
    t.left(90)
