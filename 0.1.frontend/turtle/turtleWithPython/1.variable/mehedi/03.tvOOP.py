from turtle import *

class DrawCircle:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        

    def draw(self):
        self.t = Turtle()
        self.t.color(self.color)
        self.t.circle(self.size)
    
        done()

circle = DrawCircle(color="red", size=50)

circle.draw()