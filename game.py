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
        myAns.create_word()
        self.ansWord = myAns.ansWord
        print("Answer: ",self.ansWord)
        self.guessWord = ""
        self.y = 0
        self.x = 0
        self.isOver = False
        """
        self.board = []
        for j in range(self.guessLimit):
            tmp = []
            for i in range(self.wordLength):
                tmp.append("")
            self.board.append(tmp)
        """


    def vendor_board(self):
        eel.vendorBoard(self.guessLimit, self.wordLength)

    def input(self, key):
        if(self.isOver):
            pass
        if(self.x == self.wordLength):
            if(key!="Enter" and key!="BackSpace"):
                eel.webAlert("Word is too long...")
            if(key == "Enter"):
                self.checkAns()
            if(key == "BackSpace"):
                if(self.x != 0):
                    self.x -= 1
                    self.guessWord = self.guessWord[:self.x]
                    self.modify_board(eel.modifyBoard(self.y, self.x, self.guessLimit, self.wordLength, ""))
                print("BackSpace")

        elif(key == "Enter"):
            print("Enter")
            if(self.x == self.wordLength):
                self.checkAns()

            if(self.x < self.wordLength):
                eel.webAlert("Word is too short...")

        elif(key == "BackSpace"):
            if(self.x != 0):
                self.x -= 1
                self.guessWord = self.guessWord[:self.x]
                self.modify_board(eel.modifyBoard(self.y, self.x, self.guessLimit, self.wordLength, ""))
            print("BackSpace")
        else:
            self.modify_board(key)
            self.guessWord += key
            print(key)
            self.x+=1

    def modify_board(self, key):
        eel.modifyBoard(self.y, self.x, self.guessLimit, self.wordLength, key)

    def checkAns(self):
        self.wordColor = [0 for _ in range(self.wordLength)]
        if(self.guessWord == self.ansWord):
            self.isOver = True
            self.wordColor = [2 for _ in range(self.wordLength)]
            eel.drawColor(self.y, self.wordLength, self.wordColor)
            self.y += 1
            self.x = 0
            eel.webAlert("Correct")
        #elif(wordNotExist):
        else:
            eel.drawColor()
            self.y += 1
            self.x = 0
            eel.webAlert("Please Guess again")

        self.guessWord = ""    
    
