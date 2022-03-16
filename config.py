import json

class config:

    def __init__(self):
        self.settingPath = "setting.json"
        self.loadSetting()
        
    def loadSetting(self):
        try:
            file = open(self.settingPath, 'r')
            settingJson = file.read()
            settingDict = json.loads(settingJson)
            self.wordLength = settingDict["wordLength"]
            self.guessLimit = settingDict["guessLimit"]

        except FileNotFoundError:
            print("setting.json is not existed")
            self.create_setting()
            self.wordLength = 5
            self.guessLimit = 6

    def create_setting(self):
        settingDict = {"wordLength":5, "guessLimit":6}
        settingJson = json.dumps(settingDict)
        file = open(self.settingPath, 'w')
        file.write(settingJson)
        file.close()
        