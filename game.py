from turtle import Screen
from paddle import T_paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvheight=600, canvwidth=800)
screen.title("Pong")
screen.tracer(0)

paddle_left = T_paddle((-390, 0))
paddle_right = T_paddle((390, 0))
ball = Ball()


screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")



game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # if ball.xcor() > 350:
    #     ball.bounce()
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.bounce_y()

    if ball.distance(paddle_right) < 25 and ball.xcor() > 330 or ball.distance(paddle_left) < 25 and ball.ycor() < 330:
        ball.bounce_x()



screen.exitonclick()