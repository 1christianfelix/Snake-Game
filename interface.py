from turtle import Turtle
from turtle import Screen
import time


class Interface(Turtle):

    def __init__(self):
        super().__init__()
        self.scoreboard = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.update()
        # self.reset = False
        self.reset()
        screen = Screen()

    def update(self):
        self.clear()
        self.write(f"Score: {self.scoreboard} | High Score: {self.highscore}", False, align="center",
                   font=("Arial", 12, "normal"))
        self.hideturtle()

    def reset(self):
        if self.scoreboard > self.highscore:
            with open("data.txt", mode='w') as file:
                self.highscore = self.scoreboard
                file.write(f"{self.highscore}")
        self.scoreboard = 0
        self.update()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Arial", 24, "normal"))
    #     self.goto(0, -50)
    #     self.write("Y play again | Q to quit", align="center", font=("Arial", 24, "normal"))
    #     self.screen.listen()
    #     while True:
    #         self.screen.onkey(self.end, "q")
    #         self.screen.onkey(self.gameReset, "y")
    #
    # def gameReset(self):
    #     self.reset = True
    #     self.scoreboard = 0
    #     time.sleep(.1)

    def end(self):
        print("test")
