from openal import *

class Audio:
    def __init__(self, audioPath, position, gain):
        self.audioPath = "sounds\\" + audioPath + ".wav"
        self.position = position
        self.gain = gain
        self.source = oalOpen(self.audioPath)

    def play(self):
        self.source.set_position(self.position)
        self.source.set_gain(self.gain)
        self.source.play()

    def stop(self):
        if self.source.get_state() == AL_PLAYING:
            self.source.stop()

