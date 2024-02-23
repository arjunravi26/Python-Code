import time
from turtle import Screen

from food import Food
from score_board import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
screen.update()
is_game_on = True
snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.left_move, "Left")
screen.onkey(snake.right_move, "Right")
screen.onkey(snake.up_move, "Up")
screen.onkey(snake.down_move, "Down")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < - 300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.reset()
        snake.reset()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
