from turtle import Turtle, Screen

colors = ["red", "blue", "green"]

t = Turtle()
t.color(colors[0])
t.forward(100)
t.color(colors[1])
t.right(90)
t.forward(100)
t.color(colors[2])
t.right(90)
t.forward(100)

screen = Screen()
screen.mainloop()