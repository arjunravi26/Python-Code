from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = 'center'


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.highest_score = 0
        self.high_score()
        self.color('white')
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score {self.highest_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()

    def high_score(self):
        with open('high_score.txt', mode='r') as file:
            self.highest_score = int(file.read())
