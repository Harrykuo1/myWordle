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
        self.y = 0
        self.x = 0
        for j in range(self.guessLimit):
            tmp = []
            for i in range(self.wordLength):
                tmp.append(chr(ord('A')+j*3+i))
            self.board.append(tmp)


    def vendor_board(self):
        eel.vendorBoard(self.guessLimit, self.wordLength)
        print(self.board)

    def input(self, key):

        if(self.x == self.wordLength):
            if(key != "Enter"):
                eel.webAlert("Word is too long...")
            if(key == "Enter"):
                self.y += 1
                self.x = 0

        elif(key == "Enter"):
            print("Enter")
            if(self.x == self.wordLength):
                self.y += 1
                self.x = 0
            if(self.x < self.wordLength):
                eel.webAlert("Word is too short...")

        elif(key == "BackSpace"):
            if(self.x != 0):
                self.x -= 1
                self.modify_board(eel.modifyBoard(self.y, self.x, self.guessLimit, self.wordLength, ""))
            print("BackSpace")
        else:
            self.modify_board(key)
            print(key)
            self.x+=1

    def modify_board(self, key):
        eel.modifyBoard(self.y, self.x, self.guessLimit, self.wordLength, key)
        print("modify")
    
