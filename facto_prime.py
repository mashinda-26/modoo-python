x = int(input("?"))
d = 2   # 가장 작은 소수인 2부터 나누자

while d <= x:
    if x % d == 0:
        print(d)    # d는 x의 약수
        x = x / d
    else:
        d = d + 1   # 나누어지지 않으면 1을 더해서 반복