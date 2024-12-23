from turtle import *

class MK:
    def __init__(self, size):
        self.t = Turtle()
        self.size = size
        self.colors = ["red", "blue", "yellow", "green"]

    def square(self):
        for i in range (4):
            self.t.color(self.colors[i])
            self.t.forward(self.size)
            self.t.right(90)

    def finish(self):
        done()

mk = MK(size=150)
mk.square()
mk.finish()
