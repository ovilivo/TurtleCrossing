from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(150, 270)
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increse_level(self):
        self.level +=1
        self.updateScore()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
