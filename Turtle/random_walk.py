from turtle import Turtle, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

timmy=Turtle()
screen=Screen()

def move_left():
    timmy.left(90)
    timmy.forward(40)

def move_straight():
    timmy.forward(40)

def move_right():
    timmy.right(90)
    timmy.forward(40)

movements=[move_left, move_right, move_straight]

timmy.speed(0)


for _ in range(0,100):
    timmy.pensize(10)
    timmy.color(random.choice(colours))
    move=random.choice(movements)
    move()


screen.exitonclick()

