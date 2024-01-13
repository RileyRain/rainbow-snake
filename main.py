from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food

# classic snake game with a rainbow theme
# wasd to control snake
# functional high score system from data.txt


def snake_game():
    screen = Screen()
    screen.title("Rainbow Snake by Rai")
    screen.setup(width=600, height=600)
    screen.bgcolor("Black")
    screen.tracer(0)

    scoreboard = Scoreboard()
    food = Food()

    snake = Snake()

    screen.listen()
    screen.onkeypress(snake.go_left, "a")
    screen.onkeypress(snake.go_right, "d")
    screen.onkeypress(snake.go_up, "w")
    screen.onkeypress(snake.go_down, "s")

    screen.update()
    snake.clear()

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()

            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset_snake()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset_snake()

    screen.exitonclick()


snake_game()
