from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(x=0, y=-250)
        self.left(90)

    def move_turtle(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def reset(self):
        self.goto(x=0, y=-250)
