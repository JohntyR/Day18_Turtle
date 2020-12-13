from turtle import Turtle, Screen
from shape import Shape

timmy = Turtle()
timmy.shape("turtle")
timmy.color("dark magenta")
timmy.pensize(4)
timmy.speed("fastest")
timmy.penup()
timmy.forward(200)
timmy.left(90)
timmy.forward(200)
timmy.right(90)
timmy.pendown()

my_shapes = [
    {"name": "Triangle", "sides": 3, "colour": "plum"},
    {"name": "Square", "sides": 4, "colour": "orchid"},
    {"name": "Pentagon", "sides": 5, "colour": "medium orchid"},
    {"name": "Hexagon", "sides": 6, "colour": "dark orchid"},
    {"name": "Septagon", "sides": 7, "colour": "dark violet"},
    {"name": "Octagon", "sides": 8, "colour": "blue violet"},
    {"name": "Nonagon", "sides": 9, "colour": "medium purple"},
]

shape_bank = []

for s in my_shapes:
    shape_bank.append(Shape(s["sides"], s["colour"]))


for i in range(1, 10):
    for s in shape_bank:
        timmy.pencolor(s.colour)
        for j in range(s.sides):
            timmy.right(s.angle)
            timmy.forward(i * 10)


screen = Screen()
screen.exitonclick()