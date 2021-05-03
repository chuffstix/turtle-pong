from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.side = side
        self.penup()
        self.hideturtle()
        self.color("white")
        if self.side == "p1":
            self.goto(-30, 360)
        if self.side == "p2":
            self.goto(30, 360)
        self.write(str(self.score), align="center", font=("Arial", 30, "bold"))

    def add_point(self):
        self.clear()
        self.score += 1
        self.write(str(self.score), align="center", font=("Arial", 30, "bold"))

