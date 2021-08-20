from turtle import *

pensize(1)
speed(0)

def draw(seitenlaenge, abstand):
    s = seitenlaenge
    penup()
    goto(-s/2, s/2)
    pendown()
    while s > 0:
        for i in [1,2]:    
            forward(s)
            right(90)
        s -= abstand
        

draw(500, 5)
done()