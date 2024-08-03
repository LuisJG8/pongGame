from turtle import Screen
from paddle import T_paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvheight=600, canvwidth=800)
screen.title("Pong")
screen.tracer(0)

paddle_left = T_paddle((-390, 0))
paddle_right = T_paddle((390, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # if ball.xcor() > 350:
    #     ball.bounce()s
    if ball.ycor() > 350 or ball.ycor() < -350:
        ball.bounce_y()

    if ball.distance(paddle_right) < 35 and ball.xcor() > -370 or ball.distance(paddle_left) < 35 and ball.ycor() < 370:
        ball.bounce_x()

    if ball.xcor() < -440:
        ball.reset_ball()
        scoreboard.update_scoreboard()
        scoreboard.l_point()

    if ball.xcor() > 440:
        ball.reset_ball()
        scoreboard.update_scoreboard()
        scoreboard.r_point()

screen.exitonclick()