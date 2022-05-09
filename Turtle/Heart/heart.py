from turtle import *

# Creating a turtle object(pen)
bgcolor('black')
hideturtle()

# Defining a method to draw curve
def curve():
    speed(1)
    for i in range(200):
        right(1)
        forward(1)

# Defining method to draw a full heart
def heart():
    pensize(3)
    color('yellow', 'red')
    begin_fill()
    left(140)
    forward(113)
    curve()
    left(120)
    curve()
    forward(112)
    end_fill()

# Defining method to write text
def txt():
    penup()
    setpos(-68, 95)
    pendown()

# Draw a heart
heart()
txt()

done()