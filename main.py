from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("MINI PONG GAME")
screen.tracer(0)
screen.listen()
score = Scoreboard()

paddles = Paddle((380, 0))
paddles2 = Paddle((-387, 0))
balls = Ball()

screen.onkey(paddles.up, "Up")
screen.onkey(paddles.down, "Down")
screen.onkey(paddles2.up, "w")
screen.onkey(paddles2.down, "s")

game_on = True
while game_on:
    time.sleep(balls.move_speed)
    screen.update()
    balls.move()

    # Detecting the collision between ball with the up wall
    if balls.ycor() > 280 or balls.ycor() < -275:
        balls.bounce_y()

    # Detecting the collision between ball with the paddles
    if balls.distance(paddles) < 50 and balls.xcor() > 350 or balls.distance(paddles2) < 50 and balls.xcor() < -360:
        balls.bounce_x()

    # Detecting the right paddle miss
    if balls.xcor() > 400:
        balls.reset_ball()
        score.left_point()

    # Detecting the left paddle miss
    if balls.xcor() < -400:
        balls.reset_ball()
        score.right_point()

    # Detecting the Winner
    if score.left_score == 2:
        game_on = False
        score.winner("Left")

    if score.right_score == 2:
        game_on = False
        score.winner("Right")


screen.exitonclick()
