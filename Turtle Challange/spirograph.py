import random
from turtle import Turtle, Screen

from color_extraction import extract_color

colors = extract_color()
tim = Turtle()
tim.speed(0)
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.pendown()
tim.setheading(0)
num_of_dots = 100

for dot in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.penup()
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()

screen = Screen()
screen.exitonclick()
