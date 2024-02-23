import turtle
from turtle import Screen, Turtle

import pandas as pd

state_data = pd.read_csv('Pandas/state game/50_states.csv')
x_cor = state_data['x']
y_cor = state_data['y']
state = state_data['state']
# print(x_cor, y_cor)
print(state)

screen = Screen()
screen.title('US state game')
image = 'blank_states_img.gif'
image = 'C:/Users/Dell/OneDrive/Documents/Imp Projects/100 Days bootcamp python/Pandas/state game/blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)


def get_mouse_click_cor(x, y):
    if x in x_cor or y in y_cor:
        print(x, y)


screen.onscreenclick(get_mouse_click_cor)
guess_count = 0
while guess_count <= 50:
    answer_state = turtle.textinput(title=f"{guess_count}/Guess the state", prompt="What`s another states name").title()
    if answer_state=="Exit":
        break
    if answer_state in state.values:
        t = Turtle()
        st_data = state_data[state_data.state == answer_state]
        t.color('black')
        t.hideturtle()
        t.penup()
        t.goto(int(st_data.x), int(st_data.y))
        t.write(st_data.state.item())
        guess_count += 1

