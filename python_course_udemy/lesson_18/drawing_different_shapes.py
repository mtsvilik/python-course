from turtle import Turtle
import random

timmy = Turtle()
timmy.shape("turtle")

colors = ["tomato", "yellow", "coral", "red", "blue", "green", "pink"]


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shapes(shape_side_n)
