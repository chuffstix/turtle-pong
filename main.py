from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# setup screen
screen = Screen()
screen.tracer(False)
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("PONG")


def draw_centreline():
    line = Turtle()
    line.color("white")
    line.penup()
    line.hideturtle()
    line.goto(0, -400)
    line.setheading(90)
    for _ in range(35):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(10)

player1 = Paddle("left")
player2 = Paddle("right")
ball = Ball()
player1score = Scoreboard("p1")
player2score = Scoreboard("p2")

draw_centreline()

screen.update()

game_on = True

while game_on:
    in_play = True
    screen.listen()
    screen.onkeypress(player1.up, "w")
    screen.onkeypress(player1.down, "s")
    screen.onkeypress(player2.up, "Up")
    screen.onkeypress(player2.down, "Down")

    while in_play:
        ball.start_moving()
        # detect collision with paddles
        if ball.distance(player1) < 50 and ball.xcor() < -560 or ball.distance(player2) < 50 and ball.xcor() > 560:
            ball.bounce_off_vertical()
        # detect collision with walls
        if ball.ycor() < -390 or ball.ycor() > 390:
            ball.bounce_off_horizontal()
        # detect goal scored and add points
        if ball.xcor() < -600:
            player2score.add_point()
            ball.goto(0, 0)
            in_play = False
        if ball.xcor() > 600:
            player1score.add_point()
            ball.goto(0, 0)
            in_play = False
        #if player1score.score == 2 or player2score.score == 2:
           # game_on = False
        time.sleep(0.01)

        screen.update()

screen.exitonclick()
