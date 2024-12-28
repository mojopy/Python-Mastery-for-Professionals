from turtle import *

bgcolor("lightblue")
shape("turtle")

points = [(0, 0), (100, 0),(100, 0),(100, 100), (0,100), (0, 0)]


pen = Turtle()

pen.penup()
pen.goto(points[0])
pen.pendown()
pen.goto(points[1])
pen.goto(points[2])
pen.goto(points[3])
pen.goto(points[4])


done()