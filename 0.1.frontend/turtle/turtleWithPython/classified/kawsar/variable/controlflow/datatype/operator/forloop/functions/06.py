from turtle import *

def draw_square(lenght):
    forward(lenght)
    right(90)
    forward(lenght)
    right(90)
    forward(lenght)
    right(90)
    forward(lenght)
    right(90)


bgcolor("lightblue")

shape("turtle")
speed(2)

draw_square(100)

done()