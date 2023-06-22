# import turtle as t
from turtle import Turtle, Screen
# from turtle import *


timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

for _ in range(3):
    timmy.forward(100)
    timmy.left(120)

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

for _ in range(6):
    timmy.backward(100)
    timmy.right(60)

for _ in range(8):
    timmy.forward(100)
    timmy.right(45)

screen = Screen()
screen.exitonclick()
