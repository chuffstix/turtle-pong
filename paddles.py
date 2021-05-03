from turtle import Turtle
''' The paddle class takes one argument, either left or right. 
It can be sent up and down the screen on the y-axis'''


class Paddle(Turtle):
    # Paddle instance requires a side, left or right
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.color("white")
        self.penup()
        self.side = side
        self.send_to_side()

    def send_to_side(self):
        if self.side == "left":
            self.goto(-570, 0)
        if self.side == "right":
            self.goto(570, 0)

    def up(self):
        if self.ycor() != 360:  # stop if paddle has reached top of screen
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() != -360:  # stop if paddle has reached bottom of screen
            self.goto(self.xcor(), self.ycor()-20)
