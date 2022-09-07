from turtle import Screen, Turtle

tur = Turtle()
# Draw a dashed line
# for _ in range(10):
#     tur.forward(10)
#     tur.penup()
#     tur.forward(10)
#     tur.pendown()

# Draw figures
# sides = 3
# for i in range(7):
#     tur.pencolor(random(), random(), random())
#     for j in range(sides):
#         tur.forward(100)
#         tur.right(360/sides)
#     sides += 1

# Random shit (Random walk)
# tur.width(20)
# tur.speed("fastest")
# angles = [0, 90, 180, 270]
# for _ in range(50):
#     tur.color(random(), random(), random())
#     tur.forward(50)
#     tur.setheading(choice(angles))
#     tur.forward(50)

# Circles
# angle = 0
# tur.speed("fastest")
# for _ in range(101):
#     tur.color(random(), random(), random())
#     tur.circle(100)
#     tur.setheading(angle)
#     angle += 3.6

screen = Screen()
screen.exitonclick()
