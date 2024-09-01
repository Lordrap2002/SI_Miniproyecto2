from sys import stdin

class Line:
    def __init__(self, lineNumber, sounds):
        self.lineNumber = lineNumber
        self.text = self.getText()
        self.sounds = sounds
    
    def getText(self):
        with open("history.txt", 'r') as file:
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