class animal:
    def __init__(self, breathe, move):
        self.breathe = True
        self.move = True
    
    def alive(self):
        self.breathe = True
        
    def dead(self):
        self.breathe = False
    
class cat(animal):
    
    def meow(self):
        print("meow")