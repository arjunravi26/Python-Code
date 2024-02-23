import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from score import Score

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
paddle_right = Paddle(350)
paddle_left = Paddle(-350)
screen.listen()
ball = Ball()
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
score = Score()
key = 0.1
is_game_on = True
while is_game_on:
    time.sleep(key)
    screen.update()
    ball.move()

    # Detection collision with the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        score.update_left_scoreboard()
        ball.reset()
    if ball.xcor() < -400:
        score.update_right_scoreboard()
        ball.reset()


screen.exitonclick()
