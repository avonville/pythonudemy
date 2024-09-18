import colorgram
import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

# Extract 6 colors from an image.
colors = colorgram.extract('Day18/hurst.jfif', 15)

color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r, g, b))

tim = Turtle()
tim.shape("turtle")

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1 ):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()

screen.exitonclick()

