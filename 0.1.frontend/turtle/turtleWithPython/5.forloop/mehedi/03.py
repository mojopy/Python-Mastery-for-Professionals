from turtle import *

class Make_Triangle:
    def __init__(self, size):
        self.t = Turtle()
        self.size = size
        self.colors = ["red", "yellow", "blue"]

    def draw(self):
        for i in range (3):
            self.t.forward(self.size)
            self.t.color(self.colors[i])
            self.t.right(120)

    def finish(self):
        done()

mt = Make_Triangle(size=150)

mt.draw()
mt.finish()