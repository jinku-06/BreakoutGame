from turtle import *


class Paddle(Turtle):

    def __init__(self, position: tuple):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(position)
        self.speed = 50

    def go_left(self):
        new_x = self.xcor() - self.speed
        if new_x > -350:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + self.speed
        if new_x < 350:
            self.goto(new_x, self.ycor())
