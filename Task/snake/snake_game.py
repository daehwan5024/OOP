from score import Score
from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Gshs Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Score()
screen.listen()
game_is_on = True
screen.update()
screen.onkey(snake.up, "Up")
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, "Down")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "Left")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "d")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()
    for segment in snake.snake_body[1:]:
        if (segment != snake.head) and (snake.head.distance(segment)) < 10:
            game_is_on = False
            score_board.game_over()
screen.exitonclick()
