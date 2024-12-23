from turtle import *

bgcolor("lightblue")

shape("turtle")
speed(2)

num_sides = 4
side_lenght = 100

for _ in range(num_sides):
    forward(side_lenght)
    right(90)

done()