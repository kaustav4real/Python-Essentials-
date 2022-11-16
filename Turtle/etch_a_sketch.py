from turtle import Turtle, Screen

timmy=Turtle()
screen=Screen()
screen.listen()

timmy.width(4)
timmy.shape("turtle")

def move_forwards():
    timmy.forward(10)

def clockwise():
    current_heading=timmy.heading()
    new_heading=current_heading-10
    timmy.setheading(new_heading)


def counter_clockwise():
    current_heading=timmy.heading()
    new_heading=current_heading+10
    timmy.setheading(new_heading)

def backwards():
    timmy.forward(-10)

def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.onkey(key="w", fun=move_forwards)
screen.onkeypress(key="w", fun=move_forwards)

screen.onkey(key="a", fun=counter_clockwise)
screen.onkeypress(key="a", fun=counter_clockwise)

screen.onkey(key="s", fun=backwards)
screen.onkeypress(key="s", fun=backwards)

screen.onkey(key="d", fun=clockwise)
screen.onkeypress(key="d", fun=clockwise)

screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
