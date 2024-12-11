from turtle import *

class SimpleTurtle:
    def draw_square(self):
        distance = 200
        angle = 90

        forward(distance)
        right(angle)
        forward(distance)
        right(angle)
        forward(distance)
        right(angle)
        forward(distance)

        done()

my_turtle = SimpleTurtle()
my_turtle.draw_square()