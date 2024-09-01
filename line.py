from sys import stdin
from audio import Audio

class Line:
    def __init__(self, lineNumber):
        self.lineNumber = lineNumber - 1
        self.text, self.paths, self.options, self.sounds = self.getData()
    
    def getData(self):
        with open("history.txt", 'r') as file:
            line = file.readlines()[self.lineNumber].split("#")
            if len(line) > 2:
                return line[0], [int(x) for x in line[1].split(",")], line[2].split(","), self.getSounds([int(x) for x in line[3].split(",")])
            else:
                return line[0], [], [], []
    
    def getSounds(self, soundLines):
        sounds = []
        with open("soundsInfo.txt", 'r') as file:
            lines = file.readlines()
            for line in soundLines:
                data = lines[line - 1].split("#")
                position = tuple([int(x) for x in data[1].split(",")])
                sounds.append(Audio(data[0], position))
        return sounds
        
    def __str__(self):
        return self.text
        
    def playSounds(self):
        for sound in self.sounds:
            sound.play()
    
    def stopSounds(self):
        for sound in self.sounds:
            sound.stop()