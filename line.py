from sys import stdin

class Line:
    def __init__(self, type, lineNumber, sounds):
        self.type = type
        self.lineNumber = lineNumber
        self.text = self.getText()
        self.sounds = sounds
    
    def getText(self):
        if self.type:
            path = "history.txt"
        else:
            path = "dialogue.txt"
        with open(path, 'r') as file:
            lines = file.readlines()
            return lines[self.lineNumber]
        
    def __str__(self):
        return self.text
        
    def playSounds(self):
        for sound in self.sounds:
            sound.play()
    
    def stopSounds(self):
        for sound in self.sounds:
            sound.stop()