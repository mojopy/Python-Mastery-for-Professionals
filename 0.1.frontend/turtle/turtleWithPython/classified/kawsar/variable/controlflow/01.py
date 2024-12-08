from turtle import *

bgcolor("lightblue")

shape("turtle")
speed(2)

shape_type = "triangle"

if shape_type == "triangle":

    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
elif shape_type == "square":
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
else:
    forward(100)


done()