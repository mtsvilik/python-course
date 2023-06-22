from turtle import Turtle
import random

timmy = Turtle()
timmy.shape("turtle")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
directions = [0, 90, 180, 270]

timmy.speed("fast")
timmy.pensize(15)

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
