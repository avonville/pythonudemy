# Create a spirograph using turtle graphics
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
    change_color()


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    tim.color(R, G, B)

def draw_dashed_line():
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def random_walk():
    tim.pensize(10)
    tim.speed(10)
    for _ in range(100):
        tim.color(random.random(), random.random(), random.random())
        tim.forward(30)
        tim.setheading(random.choice([0, 90, 180, 270]))

# random_walk()

def draw_spirograph(size_of_gap):
    tim.speed(10)
    for _ in range(int(360 / size_of_gap)):
        tim.color(random.random(), random.random(), random.random())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()
