from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
place = -100
turtles = []
is_over = False

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-240, place+30)
    place = place+30
    turtles.append(new_turtle)

while not is_over:
    for turtle in turtles:
        turtle.forward(random.randint(0, 30))
        print(turtle.pos())
        if (turtle.xcor() >= 230):
            if (turtle.pencolor() == user_bet):
                print(f"{turtle.pencolor()} is the winner!!")
            else:
                print(f"You lost.... {turtle.pencolor()} is the winner!")
            is_over = True
            break

screen.exitonclick()
