from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.speed("fastest")

    def move(self):
        if ((self.ycor() < 290) and (self.xcor() < 390)):
            self.goto(self.xcor() + 10, self.ycor() + 10)
            print("y: ", self.ycor())
            print("x: ", self.xcor())
