from turtle import *

class MyTurtle:
    def __init__(self, color, size):
        self.t = Turtle ()
        self.t.color(color)
        self.size = size
        self.t.speed(3)

    def make_star(self):
        for i in range (5):
            self.t.forward(self.size)
            self.t.right(144)

    def finish(self):
        done()

trl = MyTurtle(color="yellow", size=150)

trl.make_star()
trl.finish()