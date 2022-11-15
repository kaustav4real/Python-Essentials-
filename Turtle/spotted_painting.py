import turtle as t
from turtle import Turtle,Screen
import random

color_list=[(246, 240, 227), (249, 236, 244), (232, 246, 238), (235, 240, 248), (199, 152, 116), (142, 70, 88), (227, 217, 107), (59, 97, 131), (147, 81, 67), (134, 165, 187), (189, 144, 160), (34, 20, 14), (20, 27, 43), (132, 177, 149), (199, 91, 77), (196, 81, 99), (47, 24, 34), (50, 124, 94), (13, 25, 18), (76, 160, 111), (227, 170, 184), (114, 40, 60), (172, 161, 57), (230, 172, 164), (48, 55, 99), (164, 210, 185), (224, 222, 12), (54, 158, 179), (112, 121, 160), (175, 188, 218)]

t.colormode(255)

timmy=Turtle()

screen=Screen()
timmy.penup()
timmy.hideturtle()
timmy.speed(0)

timmy.right(90)
timmy.forward(150)
timmy.left(90)

def start_new_line():
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)

def draw_dots():
    for dots in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    start_new_line()

for y in range(0,10):
    draw_dots()

screen.exitonclick()
