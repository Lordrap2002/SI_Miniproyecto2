import openal as al
import time

class audio:
    def __init__(self, audioPath, position, duration):
        self.audioPath = audioPath
        self.position = position
        self.duration = duration
    
    def play(self):
        buffer = al.oalOpen(self.audioPath)
        source = al.oalGetSource()
        source.set_buffer(buffer)
        source.set_position(self.position)
        source.play()
        while source.get_state() == al.AL_PLAYING:
            time.sleep(self.duration)
        source.delete()
        buffer.delete()