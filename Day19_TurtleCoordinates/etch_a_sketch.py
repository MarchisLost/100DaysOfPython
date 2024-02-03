from turtle import Screen, Turtle

tur = Turtle()


def move_forward():
    tur.forward(10)


def move_backwards():
    tur.bk(10)


def move_right():
    tur.right(10)


def move_left():
    tur.left(10)


def clear():
    tur.reset()


screen = Screen()
screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backwards)
screen.onkeypress(key='d', fun=move_right)
screen.onkeypress(key='a', fun=move_left)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
