import json

class config:

    def __init__(self):
        self.settingPath = "setting.json"
        self.loadSetting()
        
    def loadSetting(self):
        try:
            file = open(self.settingPath, 'r')
            settingJson = file.read()
            self.settingDict = json.loads(settingJson)
            self.wordLength = self.settingDict["wordLength"]
            self.guessLimit = self.settingDict["guessLimit"]
            self.timeLimit = self.settingDict["timeLimit"]

        except FileNotFoundError:
            print("setting.json is not existed")
            self.create_setting()
            self.wordLength = 5
            self.guessLimit = 6
            self.timeLimit = 60

    def create_setting(self):
        settingDict = {"wordLength":5, "guessLimit":6, "timeLimit":60}
        settingJson = json.dumps(settingDict)
        file = open(self.settingPath, 'w')
        file.write(settingJson)
        file.close()

    def saveSetting(self, wordLength, guessLimit, timeLimit):
        wordLength = int(wordLength)
        guessLimit = int(guessLimit)
        timeLimit = int(timeLimit)
        self.wordLength = wordLength
        self.guessLimit = guessLimit
        self.timeLimit = timeLimit
        self.settingDict["wordLength"] = wordLength
        self.settingDict["guessLimit"] = guessLimit
        self.settingDict["timeLimit"] = timeLimit
        settingJson = json.dumps(self.settingDict)
        print("Save:", settingJson)
        file = open(self.settingPath, 'w')
        file.write(settingJson)
        file.close()


        