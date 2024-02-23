import random
from turtle import Turtle, Screen
from generate_color import color_generate
tim = Turtle()
tim.pensize(3)
tim.speed(0)
directions = [0, 90, 180, 270]





#
for i in range(200):
    tim.color(color_generate())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

# def draw_shape(num_sides, color_of_shape):
#     for _ in range(num_sides):
#         tim.color(color_of_shape)
#         tim.forward(100)
#         tim.left(360 / num_sides)
#
#
# # for _ in range(10):
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
#
# colors = ["chartreuse", "fuchsia", "teal", "turquoise", "indigo", "maroon", "olive", "sienna"]
# for i in range(3, 10):
#     color = random.choice(colors)
#     draw_shape(i, color)
