from turtle import *

class BangladeshFlag:
    def __init__(self):
        self.t = Turtle()
        self.screen = Screen()
        self.screen.bgcolor("white")  # Set background color
        self.t.speed(5)  # Set turtle speed

    def draw_rectangle(self):
        """Draws the green rectangular background."""
        self.t.penup()
        self.t.goto(-150, 100)  # Starting position
        self.t.pendown()
        self.t.color("green")
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(300)  # Rectangle width
            self.t.right(90)
            self.t.forward(200)  # Rectangle height
            self.t.right(90)
        self.t.end_fill()

    def draw_circle(self):
        """Draws the red circle in the flag."""
        self.t.penup()
        self.t.goto(-50, 30)  # Position for the center of the circle
        self.t.pendown()
        self.t.color("red")
        self.t.begin_fill()
        self.t.circle(50)  # Circle radius
        self.t.end_fill()

    def finish(self):
        self.t.hideturtle()  # Hide the turtle
        self.screen.mainloop()  # Keep the window open

# Create the flag object and draw the flag
flag = BangladeshFlag()
flag.draw_rectangle()
flag.draw_circle()
flag.finish()
