from turtle import Turtle, colormode
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        rand_x = random.randint(-260, 260)
        rand_y = random.randint(-260, 260)
        self.goto(rand_x, rand_y)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-260, 260)
        rand_y = random.randint(-260, 260)
        self.color(random.choice(COLORS))
        self.goto(rand_x, rand_y)

