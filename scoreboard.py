from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-80, 200)
        self.write(self.left_score, align="center", font=("Courier", 70, "normal"))
        self.goto(80, 200)
        self.write(self.right_score, align="center", font=("Courier", 70, "normal"))

    def left_point(self):
        self.left_score += 1
        self.score_update()

    def right_point(self):
        self.right_score += 1
        self.score_update()

    def winner(self, player_win):
        self.goto(0, 0)
        self.write(f"Player {player_win} Win The Game !", align="center", font=("Courier", 30, "normal"))