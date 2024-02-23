from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_score_board()

    def update_left_scoreboard(self):
        self.l_score += 1
        self.show_score_board()

    def update_right_scoreboard(self):
        self.r_score += 1
        self.show_score_board()

    def show_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f'{self.l_score}', align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(arg=f'{self.r_score}', align='center', font=('Courier', 80, 'normal'))
