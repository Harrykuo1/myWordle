import eel

@eel.expose
class game:
    def __init__(self):
        #讀取設定（）
        self.init_game()

    def init_game(self):
        self.guessLimit = 6
        self.wordLength = 5
        self.guessWord = ""
        print("init")

    def input(self, key):
        print(key)
    
