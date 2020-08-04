import turtle as t

def polygon(n):
    for x in range(n):
        t.fd(50)
        t.lt(360/n)

def polygon2(n, a):
    for x in range(n):
        t.fd(a)
        t.lt(360/n)

t.hideturtle()  #거북이를 화면에서 숨긴다.

polygon(3)
polygon(5)

t.up()  #그림 그리지 않고
t.fd(100)   #거북이를 100만큼 이동
t.down()    #그림 준비

polygon2(3, 75) #한 변이 75인 삼각형
polygon2(5, 100)    #한 변이 100인 오각형