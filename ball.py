from turtle import Turtle
import random as r


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(r.randrange(0, 360, 9))
        self.tiltangle(360-self.heading())

    def start_moving(self):
        self.forward(10)

    def bounce_off_vertical(self):
        angle_of_incidence = self.heading()
        angle_of_reflection = (360 - angle_of_incidence + 180) % 360
        self.setheading(angle_of_reflection)

    def bounce_off_horizontal(self):
        angle_of_incidence = self.heading()
        angle_of_reflection = (360 - angle_of_incidence)
        self.setheading(angle_of_reflection)
