from turtle import Turtle, done

t = Turtle()

colors = ["red", "green", "yellow", "blue"]

for color in colors:
    if color == "yellow":
        print("Skipping yellow!")
        continue

    t.color(color)
    t.forward(100)
    t.right(90)

done()