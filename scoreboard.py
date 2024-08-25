from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score}  Lives: {self.lives} Restart: press 'r' ",
            align="center",
            font=("Courier", 24, "normal"),
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def decrease_life(self):
        self.lives -= 1
        self.update_scoreboard()
