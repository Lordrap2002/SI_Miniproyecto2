import os
from openal import * 
from pydub import AudioSegment

def get_audio_duration(filename):
    audio = AudioSegment.from_file(filename)
    return len(audio) / 1000.0

class Audio:
    def __init__(self, audioPath, position):
        self.audioPath = os.path.join("sounds", audioPath + ".wav")
        self.position = position
        self.duration = get_audio_duration(self.audioPath)
        self.source = oalOpen(self.audioPath)

    def play(self):
        self.source.set_position(self.position)
        self.source.set_gain(1)
        self.source.play()

    def stop(self):
        if self.source.get_state() == AL_PLAYING:
            self.source.stop()

