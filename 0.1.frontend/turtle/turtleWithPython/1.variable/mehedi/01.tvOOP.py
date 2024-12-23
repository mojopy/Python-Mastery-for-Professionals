from turtle import *

class MyDrawing:
    def __init__(self, color, distance):
        self.color = color
        self.distance = distance
        self.t = Turtle()

    def move(self):
        self.t.forward(self.distance)
        self.t.color(self.color)

    def finish(self):
        done()

drawing = MyDrawing(color="blue", distance=50)

drawing.move()
drawing.finish()