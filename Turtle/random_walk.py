import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)
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

def change_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

for _ in range(0,100):
    timmy.pensize(10)
    timmy.color(change_color())
    move=random.choice(movements)
    move()


screen.exitonclick()

