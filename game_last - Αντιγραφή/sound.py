import pygame

class SoundPlayer:
    def __init__(self, sound_path):
        self.sound = pygame.mixer.Sound(sound_path)
        self.volume = 1  # Default volume

    def play(self):
        self.sound.play()

    def stop(self):
        self.sound.stop()

    def set_volume(self, volume):
        self.volume = volume
        self.sound.set_volume(self.volume)

    def loop(self, loops=-1):
        self.sound.play(loops=loops)

    def get_duration(self):
        return self.sound.get_length()