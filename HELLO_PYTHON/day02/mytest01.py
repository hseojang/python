


a = input("첫 수를 입력하세요 : ")
b = input("끝 수를 입력하세요 : ")
m = input("배수를 입력하세요 : ")

aa = int(a)
bb = int(b)
mm = int(m)

sum = 0

arr = range(aa, bb+1)

# m의 배수는 m으로 나누었을 때 0이 되는 수임을 이용해야 한다.
for i in arr:
    if i%mm==0:
        sum+=i

print(sum)