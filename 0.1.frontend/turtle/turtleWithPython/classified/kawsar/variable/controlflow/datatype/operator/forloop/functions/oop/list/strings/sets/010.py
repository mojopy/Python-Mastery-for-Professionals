from turtle import *

bgcolor("lightblue")
shape("turtle")
speed(3)

points ={(0, 0), (100, 0), (100, 100), (0, 100)}

ordered_points = list(points)

pen = Turtle()

pen.penup()
pen.goto(ordered_points[0])
pen.pendown()
pen.goto(ordered_points[1])
pen.goto(ordered_points[2])
pen.goto(ordered_points[3])
pen.goto(ordered_points[0])

done()