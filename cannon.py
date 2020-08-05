import turtle as t
import random

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def blank():
    t.clear()

def fire():
    ang = t.heading()   #현재 바라보는 각도를 구해서 변수에 저장
    while t.ycor() > 0: #거북이가 땅 위에 있는동안 반복
        t.forward(15)
        t.right(5)

    #while 반복문을 빠져나오면 거북이가 땅에 닿은 상태
    d = t.distance(target, 0)
    #성공 또는 실패를 표시할 위치
    t.sety(random.randint(10,100))
    if d < 25:
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("Bad!", False, "center", ("", 15))
    #거북이 원위치
    t.color("black")
    t.goto(-200, 10)
    t.setheading(ang)

#땅을 그리자
t.goto(-300,0)
t.down()
t.goto(300,0)
#목표 지점 설정
target = random.randint(50,150)
t.pensize(3)
t.color("green")
t.up()
t.goto(target-25,2)
t.down()
t.goto(target+25,2)
#거북이 원위치
t.color("black")
t.up()
t.goto(-200,10)
t.setheading(20)

t.speed(5)  #숫자가 커질수록 빨라짐(단, Max = 0)
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")
t.onkeypress(fire, "space")
t.listen()  # 거북이 그래픽 창이 키보드 입력을 받도록 한다.

t.mainloop()    #거북이 그래픽 창을 종료할 때까지 마우스나 키보드 입력을 계속 처리하도록 하는 함수