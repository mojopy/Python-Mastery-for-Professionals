from turtle import *

class MakeTriangle:
    def __init__(self, color, length):
        self.color = color
        self.length = length
        self.t = Turtle()
        self.t.color(self.color)

    def triangle(self):
        for i in range(3):
            self.t.forward(self.length)
            self.t.left(120)

    def finish(self):
        done()

tng = MakeTriangle(color="pink", length=100)

tng.triangle()
tng.finish()