from sys import stdin

class Line:
    def __init__(self, textPath, type, lineNumber):
        self.textPath = textPath
        self.type = type
        self.lineNumber = lineNumber
        self.text = self.getText(self)
    
    def getText(self):
        if self.type:
            path = "history.txt"
        else:
            path = "dialogue.txt"
        with open(path, 'r') as file:
            return file[self.lineNumber]