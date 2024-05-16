from turtle import Screen
import snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = snake.Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect colition with food
    if (snake.segments[0].distance(food) < 15):
        food.refresh()
        scoreboard.update()

    # Detect colition with walls
    if (snake.segments[0].xcor() <= -290 or snake.segments[0].xcor() >= 290) or (snake.segments[0].ycor() <= -290 or snake.segments[0].ycor() >= 290):
        game_is_on = False
        scoreboard.game_over()

    # Detect colition with own tail

screen.exitonclick()
