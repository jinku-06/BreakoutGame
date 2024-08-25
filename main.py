from paddle import Paddle
from turtle import Screen
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import random
import time


def reset_game():
    global game_is_on
    ball.goto(0, 0)
    ball.x_move *= -1
    ball.y_move *= -1
    scoreboard.lives = 3
    scoreboard.score = 0
    scoreboard.update_scoreboard()
    for brick in bricks:
        brick.goto(1000, 1000)
    bricks.clear()
    create_bricks()
    game_is_on = True


def create_bricks():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    for x in range(-325, 350, 70):
        for y in range(100, 250, 30):
            brick = Brick((x, y), random.choice(colors))
            bricks.append(brick)


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()
bricks = []
create_bricks()

ball.goto(paddle.xcor(), paddle.ycor() + 20)

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(reset_game, "r")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if (
        ball.distance(paddle) < 50
        and paddle.ycor() - 10 < ball.ycor() < paddle.ycor() + 10
    ):
        ball.y_move *= -1

    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.goto(1000, 1000)
            bricks.remove(brick)
            ball.y_move *= -1
            ball.increase_speed()
            scoreboard.increase_score()

    if ball.ycor() < -290:
        scoreboard.decrease_life()
        scoreboard.update_scoreboard()
        if scoreboard.lives == 0:
            game_is_on = False
            reset_game()
        else:
            ball.goto(0, 0)
            ball.y_move *= -1

screen.exitonclick()
