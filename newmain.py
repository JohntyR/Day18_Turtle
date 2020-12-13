import turtle as t
from shape import Shape
from random import randint

screen = t.Screen()
timmy = t.Turtle()
screen.colormode(255)
timmy.shape("turtle")
timmy.color("dark magenta")
timmy.pensize(10)
timmy.speed("fastest")
timmy.penup()


def gen_random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)


for i in range(10):
    timmy.setposition(-300, 300 - (i * 45))
    for j in range(10):
        timmy.color(gen_random_colour())
        timmy.dot()
        timmy.forward(45)


screen.exitonclick()