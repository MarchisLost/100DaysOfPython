from turtle import Screen, Turtle
from random import choice
import colorgram

# Extract colors from paiting
colors = colorgram.extract('Day18_Turtle/paint.png', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
tur = Turtle()
tur.speed("fastest")

screen = Screen()
screen.colormode(255)
angle = 90
posx = -450
posy = -350
tur.penup()
tur.ht()
for _ in range(10):
    tur.goto(posx, posy)
    for j in range(10):
        tur.dot(30, choice(rgb_colors))
        tur.penup()
        tur.forward(100)
    posy += 80

screen.exitonclick()
