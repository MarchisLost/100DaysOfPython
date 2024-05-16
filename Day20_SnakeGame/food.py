from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        self.goto(random.randint(2-80, 280), random.randint(-280, 280))
        self.refresh()

    def refresh(self):
        self.goto(random.randint(2-80, 280), random.randint(-280, 280))
