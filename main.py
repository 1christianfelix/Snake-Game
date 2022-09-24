from turtle import Screen
from snake import Snake
from food import Food
from interface import Interface
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snake = Snake()
food = Food()
interface = Interface()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.05)
    snake.move()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        interface.reset()
        snake.reset()

    if snake.head.distance(food) < 15:
        print("eaten")
        food.refresh()
        interface.scoreboard += 1
        interface.update()
        snake.grow()

    for _ in snake.segments:
        if _ == snake.head:
            pass
        elif snake.head.distance(_) < 10:
            interface.reset()
            snake.reset()





screen.exitonclick()

