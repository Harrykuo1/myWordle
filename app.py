import eel
import game as gm
import config as cfg

@eel.expose
def input(key):
    print("Receive key:",end=" ")
    myGame.input(key)

@eel.expose
def init_game():
    myGame.init_game()

@eel.expose
def vendor_board():
    myGame.vendor_board()

@eel.expose
def call_ans():
    ans= myGame.getAns()
    print(ans)
    eel.showAnswer(ans)

@eel.expose
def save_setting(wordLength, guessLimit):
    myGame.saveSetting(wordLength, guessLimit)


myGame = gm.game()
eel.init("web")
eel.start("menu.html", mode="my_portable_chromium", port=9487)



