from turtle import *


class TurtleArt:
    def __init__(self):
        self.t = Turtle()
        self.screen = Screen()
        self.screen.bgcolor("lightblue")
        self.t.shape("turtle")
        self.t.speed(3)

    def draw_square(self):
        self.t.penup()
        self.t.goto(-50, -50)
        self.t.pendown()
        self.t.color("green")
        for _ in range(4):
            self.t.forward(100)
            self.t.left(90)


    def draw_triangle(self):
        self.t.penup()
        self.goto_center()
        self.t.pendown()
        self.t.color("blue")
        self.t.setheading(0)
        for _ in range(3):
            self.t.forward(100)
            self.t.left(120)

    def goto_center(self):
        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()

    def exit_on_clik(self):
        self.screen.exitonclick()

    
art = TurtleArt()
art.draw_square()
art.draw_triangle()
art.exit_on_clik()