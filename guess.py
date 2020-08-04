import random

n = random.randint(1,30)

while True:
    a = input("1부터 30까지의 숫자 입니다. ")
    x = int(a)
    if x == n:
        print("정답 입니다!")
        break
    elif x < 1 or x > 30:
        print("범위 밖의 숫자 입니다.")
    elif x > n:
        print("더 작은 숫자 입니다.")
    else:
        print("더 큰 숫자 입니다.")