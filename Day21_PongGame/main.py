from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()

screen.listen()
screen.onkey(paddle1.moveUp, "Up")
screen.onkey(paddle1.moveDown, "Down")
screen.onkey(paddle2.moveUp, "w")
screen.onkey(paddle2.moveDown, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)


screen.exitonclick()
