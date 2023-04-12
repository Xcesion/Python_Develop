from turtle import Turtle

ALIGNMENT = "center"
FONT=("Airal", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.speed("fastest")
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def add(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align= ALIGNMENT, font= FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()


    def game_over(self):
        self.home()
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)