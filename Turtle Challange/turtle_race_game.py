import random
from turtle import Turtle, Screen

forward_list = [50, 10, 20, 30, 40 - 10, -5]
list_of_turtle = []
turtle_names = ['tim_1', 'tim_2', 'tim_3', 'tim_4']
colors = ['red', 'yellow', 'pink', 'orange']
y_position = 200
i = 0
is_race_on = False
screen = Screen()
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race, Enter a colour:')


def on_left_align(y_pos, index):
    name = Turtle('turtle')
    name.color(colors[index])
    name.penup()
    name.setpos(x=-390, y=y_pos)
    return name


for names in turtle_names:
    list_of_turtle.append(on_left_align(y_position, i))
    y_position -= 100
    i += 1

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in list_of_turtle:
        turtle.forward(random.choice(forward_list))
        if turtle.xcor() >= 230:
            is_race_on = False
            print(f'{turtle.pencolor()} win the race!')
            if turtle.pencolor() == user_bet:
                print(f'you win')
            else:
                print(f'you fail')

screen.setup(width=800, height=600)
screen.exitonclick()
