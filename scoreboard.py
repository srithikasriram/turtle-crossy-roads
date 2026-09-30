from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 265)
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def inc_level(self):
        self.level+=1
        self.print_level()

    def game_over(self):
        self.home()
        self.clear()
        self.write("Game Over.", align="center", font=FONT)

