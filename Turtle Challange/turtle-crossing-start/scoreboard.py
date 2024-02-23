from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align='center', font=FONT)

    def score_board(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(x=-270, y=250)
        self.write(arg=f'Level {self.level}', align='left', font=FONT)
