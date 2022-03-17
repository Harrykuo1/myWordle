import random
from multiset import *
 
class answer:
    def __init__(self):
        pass
    
    def create_word(self, wordLength):
        """self.ansWord = ""
        for i in range(5):
            self.ansWord += chr(random.randint(65,90))"""
        wordSet = self.load_words(wordLength)
        self.ansWord = random.sample(wordSet, 1)[0].upper()
        
        self.ansSet = Multiset(self.ansWord)

    def load_words(self, wordLength):
        with open('word/'+str(wordLength)+'.txt') as word_file:
            wordSet = set(word_file.read().split())

        return wordSet
