from turtle import *

class MakeSquare:
    def __init__(self, color, length, angle):
        self.color = color
        self.length = length
        self.angle = angle
        self.t = Turtle()
        self.t.color(self.color)
    
    def draw_square(self):
        for i in range (4):
            self.t.forward(self.length)
            self.t.right(self.angle)
            

    def finish(self):
        done()

square = MakeSquare(color="green", length=100, angle=90)

square.draw_square()
square.finish()