from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle((380, 0))
paddle2 = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True

while game_is_on:
    speed = time.sleep(0.1)
    ball.move()
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(paddle1) < 50 and ball.xcor() > 360 or ball.distance(paddle2) < 50 and ball.xcor() < -360:
        ball.bounce_x()

    # Detect when the ball goes out of bounds
    if ball.xcor() > 400:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()
    
    if ball.xcor() < -400:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()

    # Game over
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("Game Over", align="center", font=("Courier", 80, "normal"))

screen.exitonclick()
