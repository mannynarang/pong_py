from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.penup()

        self.color("White")
        self.hideturtle()

    def score_board(self):
        self.goto(-100, 250)
        self.write(f"Score : {self.lscore}", move=False, align='left', font=('Arial', 15, 'normal'))
        self.goto(100, 250)
        self.write(f"Score : {self.rscore}", move=False, align='left', font=('Arial', 15, 'normal'))

    def l_increase_score(self):
        self.clear()
        self.lscore += 1
        self.score_board()

    def r_increase_score(self):
        self.clear()
        self.rscore += 1
        self.score_board()

