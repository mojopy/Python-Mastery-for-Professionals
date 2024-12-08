from turtle import Turtle, Screen

t = Turtle()

t.color("blue")
for _ in range (4):
    t.forward(100)
    t.left(90)

t.color("red")
t.goto(0, 100)
t.goto(50, 150)
t.goto(100, 100)
t.goto(0, 100)

screen = Screen()
screen.mainloop()