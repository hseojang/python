import random

com = ""
mine = ""
result = ""

mine = input("가위바위보를 입력하세요 : ")

rnd = random.random()

if rnd <(1/3):
    com="가위"
elif rnd<(2/3) :
    com="바위"
else :
    com="보"

if com==mine :
    result = "비겼습니다"
elif (com=="가위" and mine=="바위")or(com=="바위" and mine=="보")or(com=="보" and mine=="가위") :
    result = "이겼습니다"
else : 
    result = "졌습니다"
    
print("나 :", mine)
print("컴퓨터 :", com)
print(result)

