from turtle import *


def strauch(length, depth, angle=30):
    if depth > 0:
        forward(length/3)
        left(angle)
        strauch(length/2, depth-1)
        right(angle)
        forward(length/3)
        right(angle)
        strauch(length/2, depth-1)
        left(angle)
        forward(length/3)
        strauch(length/2, depth-1)
        pu()
        backward(length)
        pd()

speed(0)
left(90)
color(0, 1, 0)
pensize(1)

strauch(200, 6)

done()
