class LeeJY:
    def __init__(self):
        self.money = 1000000
    def earnMoney(self, money):
        self.money += money

class KimKa:
    def __init__(self):
        self.beauty = 100
    def getOlder(self):
        self.beauty -= 1
        
# 숙제 : 조현만들기
class JoH(LeeJY, KimKa):
    def __init__(self):
        LeeJY.__init__(self)
        KimKa.__init__(self)