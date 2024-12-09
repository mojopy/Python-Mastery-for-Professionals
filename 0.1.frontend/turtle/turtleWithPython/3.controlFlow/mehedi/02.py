from turtle import Turtle, done

t = Turtle()
size = 10

while size < 200:
    t.forward(size)
    t.right(45)
    size += 10

done()
