from openal import *

class Audio:
    def __init__(self, audioPath, position):
        self.audioPath = "sounds\\" + audioPath + ".wav"
        self.position = position
        self.source = oalOpen(self.audioPath)

    def play(self):
        self.source.set_position(self.position)
        self.source.set_gain(1)
        self.source.play()

    def stop(self):
        if self.source.get_state() == AL_PLAYING:
            self.source.stop()

