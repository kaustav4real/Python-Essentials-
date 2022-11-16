from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title=" Welcome to the race", prompt="Which turtle will win. Enter a colour")
user_bet=user_bet.lower()
print(user_bet)

turtles=[]
colors=["red", "green", "purple", "blue", "pink", "orange"]
race_is_on=False

for index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    y=-210 + index*70
    new_turtle.goto(-230, y)

    turtles.append(new_turtle)


if user_bet:
    race_is_on=True

while race_is_on:
    for a_turtle in turtles:
        if a_turtle.xcor()>230:
            winning_color=a_turtle.pencolor()
            race_is_on=False
            if winning_color==user_bet:
                print(f"You won. The winning turtle is {winning_color}")
            else:
                print(f"You lost.The {winning_color} turle has won the race.")
        else:
            a_turtle.forward(random.randint(1,10))


screen.exitonclick()
