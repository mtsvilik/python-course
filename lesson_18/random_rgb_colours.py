import turtle
from turtle import Turtle
import random

turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255) 
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]

timmy.speed("fast")
timmy.pensize(15)

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
