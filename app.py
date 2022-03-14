import eel


@eel.expose
def hi():
    pass
eel.init("web")
eel.start("menu.html", mode="my_portable_chromium", port=9487)

