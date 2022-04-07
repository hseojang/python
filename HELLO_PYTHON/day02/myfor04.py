

start = int(input("첫 수를 입력하세요 : "))
end = int(input("끝 수를 입력하세요 : "))
sum = 0

a = range(start, end+1)

for i in a :
    sum += i
    
print("두 수의 합은 :", sum)
print("{}에서부터 {}까지 합은 {}입니다".format(start, end, sum))
# 숫자 문자형에 상관없이 넣어줄 수 있다.
