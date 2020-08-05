import math

d = [1,2,3,4,5]
print(d)
# 평균
mean = sum(d) / len(d)
print(mean)
# 분산
vsum = 0
for x in d: # 리스트 d에 저장된 값을 하나씩 뽑아 x에 대입하면서 반복
    vsum = vsum + (x-mean)**2
var = vsum / len(d)
print(var)
# 표준편차
std = math.sqrt(var)
std = format(std, '.3f')    # 소수점 세자리로 제한
print(std)