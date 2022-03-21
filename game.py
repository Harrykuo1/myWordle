import eel
import config as cfg
import answer as ans
from multiset import *

@eel.expose
class game:
    def __init__(self):
        #讀取設定（）
        self.init_game()

    def init_game(self):
        myCfg = cfg.config()
        self.guessLimit = myCfg.guessLimit
        self.wordLength = myCfg.wordLength
        self.myAns = ans.answer()
        self.myAns.create_word(self.wordLength)
        self.ansWord = self.myAns.ansWord
        print("Answer: ",self.ansWord)
        self.guessWord = ""
        self.y = 0
        self.x = 0
        self.isOver = False
        self.ySet = set()
        self.nSet = set()
        self.yOldSet = set()
        self.nOldSet = set()
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
        if(self.y == self.guessLimit):
            self.isOver = True
        if(self.isOver):
            eel.webAlert("Game is Over!")
            return 

        if(self.x == self.wordLength):
            if(key!="Enter" and key!="BackSpace"):
                eel.webAlert("Word is too long...")
            if(key == "Enter"):
                self.checkAns()
            if(key == "BackSpace"):
                if(self.x != 0):
                    self.x -= 1
                    self.guessWord = self.guessWord[:self.x]
                    eel.modifyBoard(self.y, self.x, self.guessLimit, self.wordLength, "")
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
                eel.modifyBoard(self.y, self.x, self.guessLimit, self.wordLength, "")
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
        tmpSet = self.myAns.ansSet.copy()
        for i in range(self.wordLength):
            if(self.guessWord[i] == self.ansWord[i]):
                self.wordColor[i] = 2
                tmpSet.remove(self.guessWord[i], 1)
        for i in range(self.wordLength):
            if(self.guessWord[i] in tmpSet and self.wordColor[i] == 0):
                self.wordColor[i] = 1
                tmpSet.remove(self.guessWord[i], 1)
        

        if(self.guessWord == self.ansWord):
            self.isOver = True
            eel.drawColor(self.y, self.wordLength, self.wordColor)
            self.y += 1
            self.x = 0
            self.manageHint()
            eel.webAlert("Correct")
        elif(self.guessWord not in self.myAns.wordSet):
            eel.webAlert("Guessword is not exist\nPlease input again")
            self.x = 0
            for i in range(self.wordLength):
                eel.modifyBoard(self.y, i, self.guessLimit, self.wordLength, "")
        else:
            eel.drawColor(self.y, self.wordLength, self.wordColor)
            self.y += 1
            self.x = 0
            self.manageHint()
            eel.webAlert("Please Guess again")

        self.guessWord = ""    
    
    def manageHint(self):
        for i in range(self.wordLength):
            if(self.wordColor[i] == 1):
                self.ySet.add(self.guessWord[i])
            if(self.wordColor[i] == 0):
                self.nSet.add(self.guessWord[i])
        self.ySet = self.ySet - self.yOldSet
        self.nSet = self.nSet - self.nOldSet

        self.yList = list(self.ySet)
        self.nList = list(self.nSet)

        eel.drawLeftHint(self.yList)
        eel.drawRightHint(self.nList)

        self.yOldSet.update(self.ySet)
        self.nOldSet.update(self.nSet)



        print("n: ",self.nList)

            
