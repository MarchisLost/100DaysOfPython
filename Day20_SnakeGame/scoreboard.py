from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("cyan")
        self.hideturtle()
        self.goto((-10, 270))
        self.write("Score: 0", align="center", font=("Arial", 20, "normal"))

    def update(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 26, "normal"))
