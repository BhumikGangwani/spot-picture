import turtle
from random import choice
from collect_colors import CollectColors

colors = CollectColors()
rgb_colors = colors.extract()

my_turtle = turtle.Turtle()
my_turtle.ht()
my_turtle.speed("fastest")
x, y = -200, -250


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
for i in range(10):
    for j in range(10):
        my_turtle.dot(20, choice(rgb_colors))
        move()
    reposition()

screen = turtle.Screen()
screen.exitonclick()
