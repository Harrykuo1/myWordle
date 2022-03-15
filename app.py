import eel
import game as gm

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

myGame = gm.game()
eel.init("web")
eel.start("menu.html", mode="my_portable_chromium", port=9487)



