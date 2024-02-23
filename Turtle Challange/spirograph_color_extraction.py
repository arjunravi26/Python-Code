import random
from turtle import Turtle, Screen
from generate_color import color_generate
tim = Turtle()
tim.shape()
tim.speed(0)
r=100
def draw_spirograph(gap_size):
    for i in range(int(360/gap_size)):
        tim.setheading(tim.heading()+gap_size)
        tim.color(color_generate())
        tim.circle(r)
draw_spirograph(10)
screen = Screen()
screen.exitonclick()
