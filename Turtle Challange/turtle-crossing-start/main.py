import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.onkey(fun=player.move_turtle, key='Up')
car = CarManager()
score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_car()
    car.make_car()
    if player.ycor() > 300:
        car.level_up()
        player.reset()
        score.level += 1
        score.score_board()
    for c in car.cars:
        if player.distance(c) < 20:
            game_is_on = False
            score.game_over()
screen.exitonclick()
