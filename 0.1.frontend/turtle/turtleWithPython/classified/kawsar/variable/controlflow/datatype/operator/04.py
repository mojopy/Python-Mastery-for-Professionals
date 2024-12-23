from turtle import *

bgcolor("lightblue")

shape("turtle")
speed(2)

side_lenght = 50 + 50
angle = 360 / 4

if side_lenght ==100:
    forward(side_lenght)
    right(angle)
    forward(side_lenght)
    right(angle)
    forward(side_lenght)
    right(angle)
    forward(side_lenght)
else:
    forward(50)

done()