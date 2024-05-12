from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_body()

    def create_body(self):
        for pos in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)

    def move(self):
        for snake_body_num in range(len(self.segments) - 1, 0, -1):
            self.segments[snake_body_num].goto(self.segments[snake_body_num-1].pos())
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if (self.segments[0].heading() != 270):
            self.segments[0].setheading(90)

    def down(self):
        if (self.segments[0].heading() != 90):
            self.segments[0].setheading(270)

    def right(self):
        if (self.segments[0].heading() != 180):
            self.segments[0].setheading(0)

    def left(self):
        if (self.segments[0].heading() != 0):
            self.segments[0].setheading(180)
