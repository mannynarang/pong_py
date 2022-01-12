import time
from turtle import Turtle, Screen

import score
from paddle import Paddle
from ball import Ball
from score import Score


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball = Ball()
score = Score()
paddle_right = Paddle((350, 0))

paddle_left = Paddle((-350, 0))
screen.update()

screen.onkey(paddle_left.move_left, "a")
screen.onkey(paddle_left.move_right, "d")

screen.onkey(paddle_right.move_left, "Left")
screen.onkey(paddle_right.move_right, "Right")

screen.listen()
game_on = True
score.score_board()
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # bounce off walls
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_y()

    # bounce off paddle
    if ball.distance(paddle_right) < 50 or ball.distance(paddle_left) < 50:
        ball.bounce_x()

#point score + increase speed of ball
    if ball.xcor() > 400:
        score.l_increase_score()
        ball.reset()
    if ball.xcor() < - 400:
        score.r_increase_score()
        ball.reset()

screen.exitonclick()
