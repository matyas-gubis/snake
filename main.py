import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_over = False
while not game_over:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.incrementScore()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 \
            or snake.head.xcor() < -280 \
            or snake.head.ycor() > 280 \
            or snake.head.ycor() < -280:
        game_over = True
        scoreboard.game_over()

    # Detect collision with tail
    # if head collides with any segment of the tail trigger game over
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()


screen.exitonclick()
