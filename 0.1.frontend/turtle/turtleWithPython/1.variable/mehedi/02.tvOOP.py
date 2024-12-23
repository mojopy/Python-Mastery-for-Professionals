from turtle import *

class TurtleDrawing:
    def __init__(self, color, distance):
        self.color = color
        self.distance = distance
        self.t = Turtle()

    def draw_forward(self):
        self.t.color(self.color)
        self.t.forward(self.distance)

        done()

drawing = TurtleDrawing(color="green", distance=100)
drawing.draw_forward()