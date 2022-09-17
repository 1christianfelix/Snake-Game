from turtle import Turtle
from turtle import Screen
import time


class Interface(Turtle):

    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.update()
        self.reset = False
        screen = Screen()

    def update(self):
        self.clear()
        self.write(f"Score: {self.scoreboard}", False, align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -50)
        self.write("Y play again | Q to quit", align="center", font=("Arial", 24, "normal"))
        self.screen.listen()
        while True:
            self.screen.onkey(self.end, "q")
            self.screen.onkey(self.gameReset, "y")

    def gameReset(self):
        self.reset = True
        self.scoreboard = 0
        time.sleep(.1)

    def end(self):
        print("test")
