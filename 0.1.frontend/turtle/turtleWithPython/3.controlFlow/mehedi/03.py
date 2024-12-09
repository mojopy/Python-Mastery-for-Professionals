from turtle import Turtle, done

t = Turtle()
count = 0

while True:
    t.forward(50)
    t.right(60)
    t.forward(50)
    t.left(60)
    count += 1
    if count == 5:
        break

done()