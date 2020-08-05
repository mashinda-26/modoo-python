import random

def make_question():
    a = random.randint(1,40)
    b = random.randint(1,20)
    op = random.randint(1,4)

    q = str(a)

    if op == 1:
        q = q + "+"
    if op == 2:
        q = q + "-"
    if op == 3:
        q = q + "*"
    if op == 4:
        q = q + "%" #편의상 나머지를 구한다

    q = q + str(b)

    return q

sc1 = 0
sc2 = 0

for x in range(5):
    q = make_question() #함수 호출
    print(q)
    ans = input("=")
    r = float(ans)  #문자열을 실수로 변환

    if eval(q) == r:
        print("정답!")
        sc1 += 1
    else:
        print("오답!")
        sc2 += 1

print("정답: ", sc1, "오답: ", sc2)
if sc2 == 0:
    print("당신은 천재입니다!")