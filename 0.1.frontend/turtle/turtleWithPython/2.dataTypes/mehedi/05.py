from turtle import Turtle, Screen

t = Turtle()

t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(0, -50)
t.pendown()
t.goto(0, -100)

screen = Screen()
screen.mainloop()