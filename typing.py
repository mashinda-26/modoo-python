import random
import time

# 단어 리스트를 만들자
w = ["cat", "dog", "fox", "monkey", "mouse"]#, "panda", "frog", "snake", "wolf"]
n = 1   # 문제 번호
print("[타자게임] 준비되면 엔터!")
input()
start = time.time()

q = random.choice(w)
while n <= 5:
    print("*문제", n)
    print(q)
    x = input()
    if q == x:
        print("통과!")
        if n == 5:
            break
        n = n + 1
        w.remove(q) # 맞춘 문제는 리스트에서 삭제
        q = random.choice(w)
    else:
        print("오타! 다시 도전!")

end = time.time()
et = end - start
et = format(et, ".2f")
print("타자 시간:", et, "초")