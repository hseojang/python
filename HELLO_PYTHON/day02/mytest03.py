# 1에서 45까지의 숫자를 중복없이 6개를 뽑으세요. 로또만들기
import random

arr = list(range(1, 45+1))

lotto = []
e = 45

for i in range(6):
    
    a=arr.pop(int(random.random()*e))
    # 랜덤은 0.0이상 1.0미만을 반환하므로 45로 설정
    # int(random.random()*e)는 0부터 44를 무작위로 반환
    
    lotto.append(a)
    e -= 1

print(lotto)
