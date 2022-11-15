import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
timmy=Turtle()
screen=Screen()

timmy.pensize(3)
timmy.speed(0)

def change_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

r=70

def draw_spirograph(gap_size):
    for _ in range(0, int(360/gap_size)):
        timmy.color(change_color())
        timmy.circle(r)
        timmy.setheading(timmy.heading()+10)

draw_spirograph(10)

screen.exitonclick()
