from turtle import Turtle
FONT = ("Courier", 16, "normal")


class HighScore(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("red")
        self.goto(-250, 270)
        self.update_high_score()

    def update_high_score(self):
        self.clear()
        self.write(f"High Score : {self.high_score}", font=FONT)

    def save_high_score(self):
        pass

