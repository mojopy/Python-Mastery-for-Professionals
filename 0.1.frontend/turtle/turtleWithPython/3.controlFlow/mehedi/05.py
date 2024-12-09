from turtle import Turtle, done

t = Turtle()

radius = 10

while radius <= 100:
    t.circle(radius)
    t.penup()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.pendown()

    radius += 10

done()