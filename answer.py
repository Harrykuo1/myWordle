import random

class answer:
    def __init__(self):
        pass
    
    def create_word(self):
        self.ansWord = ""
        #self.ansSet = set()
        for i in range(5):
            self.ansWord += chr(random.randint(65,90))
        #self.ansSet([i for i in self.ansWord])
