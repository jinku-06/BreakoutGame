from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_increase = 0.5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        if self.ycor() > 290:
            self.y_move *= -1
        if self.xcor() > 390 or self.xcor() < -390:
            self.x_move *= -1

    def increase_speed(self):
        self.x_move *= self.speed_increase
        self.y_move *= self.speed_increase
