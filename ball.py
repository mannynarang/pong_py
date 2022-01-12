from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.nycor = 20
        self.nxcor = 20
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.nxcor
        new_y = self.ycor() + self.nycor

        self.goto(new_x, new_y)

    def bounce_y(self):

        self.nycor *= -1

    def bounce_x(self):

        self.nxcor *= -1
    def reset(self):
        self.setx(0)
        self.sety(0)
        self.ball_speed = self.ball_speed * 0.90



