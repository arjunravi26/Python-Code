from turtle import Screen
import time
from car import Car

screen = Screen()
screen.tracer(0)
screen.listen()
screen.setup(width=1000, height=600)
screen.bgcolor('grey')
car = Car()
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car.move_cars()
    time.sleep(2)
    car.add_positions()
screen.exitonclick()
