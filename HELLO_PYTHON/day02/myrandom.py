import random

ranNum = int(random.random()*100)
userInput = input("홀짝을 입력하세요 : ")
answer = ""
remain = ranNum%2

if remain==0:
    answer = "짝"
    
if remain==1:
    answer = "홀"

print("나 : ",userInput)    
print("컴퓨터 : ",answer)    

if answer==userInput:
    print("맞았습니다")
else:
    print("틀렸습니다")
