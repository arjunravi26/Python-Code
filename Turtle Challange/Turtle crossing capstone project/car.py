import random
from turtle import Turtle

POSITIONS = [150, 90, 30]


class Car:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.x = 0
        self.add_positions()

    def add_positions(self):
        for y_pos in POSITIONS:
            self.create_cars(y_pos)

    def create_cars(self, y_pos):
        turtle = Turtle()
        turtle.shape('square')
        turtle.color('red')
        turtle.shapesize(stretch_wid=1, stretch_len=2.5)
        turtle.penup()
        self.x = random.randint(100, 400)
        turtle.goto(self.x, y_pos)
        self.cars.append(turtle)

    def move_cars(self):
        speed = random.randint(200, 300)

        direction = random.random()
        for car in self.cars:
            car.goto(car.xcor() - speed * direction, car.ycor())
