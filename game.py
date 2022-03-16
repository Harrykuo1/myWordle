import eel
import config as cfg
import answer as ans


@eel.expose
class game:
    def __init__(self):
        #讀取設定（）
        self.init_game()

    def init_game(self):
        myCfg = cfg.config()
        self.guessLimit = myCfg.guessLimit
        self.wordLength = myCfg.wordLength
        myAns = ans.answer()
        self.ansWord = myAns.ansWord
        self.guessWord = ""
        #self.board = []
        self.y = 0
        self.x = 0
        """
        for j in range(self.guessLimit):
            tmp = []
            for i in range(self.wordLength):
                tmp.append("")
            self.board.append(tmp)
        """


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
                if(self.guessWord == self.ansWord):
                    eel.webAlert("Correct")
                else:
                    eel.webAlert("Please Guess again")
                self.guessWord = ""

        elif(key == "Enter"):
            print("Enter")
            if(self.x == self.wordLength):
                self.y += 1
                self.x = 0
                if(self.guessWord == self.ansWord):
                    eel.webAlert("Correct")
                else:
                    eel.webAlert("Please Guess again")
                self.guessWord = ""

            if(self.x < self.wordLength):
                eel.webAlert("Word is too short...")

        elif(key == "BackSpace"):
            if(self.x != 0):
                self.x -= 1
                self.modify_board(eel.modifyBoard(self.y, self.x, self.guessLimit, self.wordLength, ""))
            print("BackSpace")
        else:
            self.modify_board(key)
            self.guessWord += key
            print(key)
            self.x+=1

    def modify_board(self, key):
        eel.modifyBoard(self.y, self.x, self.guessLimit, self.wordLength, key)
        print("modify")
    
