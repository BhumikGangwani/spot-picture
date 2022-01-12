import turtle
from random import choice
from collect_colors import CollectColors

colors = CollectColors()
rgb_colors = colors.extract()

# Setup the turtle and the screen
my_turtle = turtle.Turtle()
my_turtle.ht()
my_turtle.speed("fastest")
x, y = -200, -250

screen = turtle.Screen()

# Functions to place the turtle at positions where a spot is filled
def move():
    my_turtle.pu()
    my_turtle.fd(50)
    my_turtle.pd()


def reposition():
    global y
    y += 50
    my_turtle.pu()
    my_turtle.goto(x, y)
    my_turtle.pd()


reposition()
turtle.colormode(255)

# Loop to get a 10x10 spot image from the extracted colors
for i in range(10):
    for j in range(10):
        my_turtle.dot(20, choice(rgb_colors))
        move()
    reposition()

screen.exitonclick()
