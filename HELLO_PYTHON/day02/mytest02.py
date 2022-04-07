a = input("출력할 단수를 입력하세요 : ")

aa = int(a)
arr = range(1, 9+1)

print("{}단".format(aa))
for i in arr:
    print("{}*{}={}".format(aa, i, aa*i))
