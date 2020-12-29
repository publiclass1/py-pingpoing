import turtle
import time
import winsound

_tick2_frame = 0
_tick2_fps = 20000000  # real raw FPS
_tick2_t0 = time.time()


def tick(fps=60):
    global _tick2_frame, _tick2_fps, _tick2_t0
    n = _tick2_fps/fps
    _tick2_frame += n
    while n > 0:
        n -= 1
    if time.time()-_tick2_t0 > 1:
        _tick2_t0 = time.time()
        _tick2_fps = _tick2_frame
        _tick2_frame = 0


wn = turtle.Screen()
wn.title("the sample")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

# score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 , Player 2: 0", align="center",
          font=("Courier", 24, "bold"))

# Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    if (y > 290 - 40):
        y = 290 - 40
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    if (y < -290 + 40):
        y = -290 + 40
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    if (y > 290 - 40):
        y = 290 - 40
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    if (y < -290 + 40):
        y = -290 + 40
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main


while True:
    tick(120)
    wn.update()

    # Moving balls
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    ball.color("white")
    # Bording checking

    # top wall
    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # bottom wall
    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    # right wall
    if (ball.xcor() > 395):
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(
            "Player 1: {} , Player 2: {}".format(score_a, score_b),
            align="center",
            font=("Courier", 24, "bold"))
    # left wall
    if (ball.xcor() < -390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(
            "Player 1: {} , Player 2: {}".format(score_a, score_b),
            align="center",
            font=("Courier", 24, "bold"))

    # paddle and ball collisions
    # paddle b y=350, 350 - 340 = 10 the width of paddle b
    if ((ball.xcor() > 340 and ball.xcor() < 350) and
            (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40)):
        ball.setx(340)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.color("red")
        ball.dx *= -1
    if ((ball.xcor() < -340 and ball.xcor() > -350) and
            (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40)):
        ball.setx(-340)
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
        ball.color("red")
        ball.dx *= -1
