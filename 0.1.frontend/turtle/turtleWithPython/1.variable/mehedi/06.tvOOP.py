from turtle import *

class CircleMaking:
    def __init__(self, color, size):
        self.t = Turtle()
        self.t.color(color)
        self.size = size

    def draw(self):
        self.t.begin_fill()
        self.t.circle(self.size)
        self.t.end_fill()

    def finish(self):
        done()

c = CircleMaking(color="blue", size=100)

c.draw()
c.finish()