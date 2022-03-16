import random
from multiset import *
 
class answer:
    def __init__(self):
        pass
    
    def create_word(self):
        self.ansWord = ""
        for i in range(5):
            self.ansWord += chr(random.randint(65,90))
        self.ansSet = Multiset(self.ansWord)
