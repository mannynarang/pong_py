from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xy_position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")
        self.goto(xy_position)

    def move_left(self):
        print("left key pressed")
        self.goto(self.xcor(), self.ycor() + 40)

    def move_right(self):
        print("left right pressed")
        self.goto(self.xcor(), self.ycor() - 40)
