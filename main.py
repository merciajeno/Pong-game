from turtle import Screen
from Paddle import paddle
from Ball import Ball
from ScoreBoard import score
import time
sc = Screen()
sc.tracer(0)
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("Pong")
paddle1 = paddle(350)
paddle2 = paddle(-350)
ball = Ball()
sc.listen()
paddle2_score = score(-50)
paddle1_score = score(50)
sc.onkey(paddle2.go_up, "Up")
sc.onkey(paddle2.go_down, "Down")
sc.onkey(paddle1.go_up, "w")
sc.onkey(paddle1.go_down, "s")
game_is_on = True

while game_is_on:
    sc.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()

    if ball.xcor() > 337 and ball.distance(paddle1) < 50:
        ball.hit()

    if ball.xcor() < -337 and ball.distance(paddle2) < 50:
        ball.hit()
    if ball.xcor() > 380:
        paddle2_score.count += 1
        paddle2_score.rewrite()
        ball.Reset()
    if ball.xcor() < -380:
        paddle1_score.count += 1
        paddle1_score.rewrite()
        ball.Reset()
    if paddle1_score.count == 10 or paddle2_score.count == 10:
        if paddle1_score.count == 10:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
        break


sc.exitonclick()
