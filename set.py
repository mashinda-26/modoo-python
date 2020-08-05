A = {1,2,3,4}
B = {3,4,5,6}

print(A)
print(B)

print(1 in A)   # 1이 집합 A의 원소인가?
print(6 in B)
print(len(A))

print(A | B)    # A와 B의 합집합
print(A & B)
print(A - B)

C = {x for x in range(1,11)}    # 1이상 11미만의 정수를 원소로 하는 집합 C
D = {x for x in range(1,11) if x % 3 == 0}  # 1이상 11미만의 3의 배수를 원소로 하는 집합 D

print(C)
print(D)

print(C < D)    # C는 D의 (진)부분집합인가?
print(C > D)