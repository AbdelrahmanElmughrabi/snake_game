from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#detect the collision with food:
    if snake.head.distance(food)<15:
        food.refresh()
        score.increse_score()
        snake.extend()
#detect the collision with wall:
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        score.reset()
        snake.reset()

    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)< 10:
            score.reset()
            snake.reset()
screen.exitonclick()





