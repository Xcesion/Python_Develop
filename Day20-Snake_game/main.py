from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

t = Turtle()
sc = Screen()
food = Food()
score = ScoreBoard()

sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("My Snake Game")
sc.tracer(0)

snake = Snake()
sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.clear()
        score.add()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290:
        score.reset()
        snake.rest()

    if snake.head.ycor() > 300 or snake.head.ycor() < -280:
        score.reset()
        snake.rest()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.rest()
    # if head collides with any segment in the tail:
    # trigger game

sc.exitonclick()
