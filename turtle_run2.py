import turtle as t
import random

score = 0
playing = False

te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.seth(90)

def turn_left():
    t.seth(180)

def turn_down():
    t.seth(270)

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        play()

def play():
    global score
    global playing
    t.forward(10)
    if random.randint(1, 5) == 3:   # 20% 확률
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5

    if speed > 15:
        speed = 15
    te.forward(speed)
    if t.distance(te) < 12:
        text = "Score: " + str(score)
        message("Game Over", text)
        playing = False
        score = 0
    if t.distance(ts) < 12:
        score = score + 1
        t.write(score)
        star_x = random.randint(-230,230)
        star_y = random.randint(-230,230)
        ts.goto(star_x, star_y)

    if playing:
        t.ontimer(play, 100)    # 게임 플레이중이면 0.1초 후 play함수를 실행

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0,-100)
    t.write(m2, False, "center", ("", 15))
    t.home()    # 거북이가 그린 그림은 그대로 두고, 거북이를 기본 상태(원점,오른쪽)로 돌린다.

t.title("Turtle Run")
t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[space]")

t.mainloop()