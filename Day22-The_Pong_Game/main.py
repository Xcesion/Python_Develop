from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

score = Scoreboard()
t = Turtle()
sc = Screen()

sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()


sc.listen()
sc.onkey(r_paddle.go_up, "Up")
sc.onkey(r_paddle.go_down, "Down")

sc.onkey(l_paddle.go_up, "w")
sc.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move_r()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect ball got score
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        print("make contact")
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        score.add_l_score()

    if ball.xcor() < -390:
        ball.reset_position()
        score.add_r_score()



sc.exitonclick()