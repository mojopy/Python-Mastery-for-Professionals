from turtle import *

bgcolor("lightblue")

points = {
    "start": (0, 0),
    "point1": (100, 0),
    "point2": (100, 100),
    "point3": (0, 100)
}

pen = Turtle()

pen.penup()
pen.goto(points["start"])
pen.pendown()
pen.goto(points["point1"])
pen.goto(points["point2"])
pen.goto(points["point3"])
pen.goto(points["start"])

done()