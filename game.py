import eel

@eel.expose
class game:
    def __init__(self):
        #讀取設定（）
        self.init_game()

    def init_game(self):
        self.guessLimit = 7
        self.wordLength = 6
        self.guessWord = ""
        self.board = []
        for j in range(self.guessLimit):
            tmp = []
            for i in range(self.wordLength):
                tmp.append(chr(ord('A')+j*3+i))
            self.board.append(tmp)
    def vendor_board(self):
        eel.vendorBoard(self.guessLimit, self.wordLength)
        print(self.board)


    def input(self, key):
        self.modify_board()
        print(key)

    def modify_board():
        pass
    
