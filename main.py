from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

"""
0. Create the screen
1. Create and move a paddle
2. Create another paddle
3. Create the ball and make it move
4. Detect collision with the wall and bounce
5. Detect collision with paddle
6. Detect when paddle misses
7. Keep score
"""
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Pong")

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the ball goes out of bounds at the edge of the screen
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
