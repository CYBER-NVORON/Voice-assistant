import pygame
class Music():
    pygame.mixer.init()
    background_music=pygame.mixer.music
    background_music.load("resources/Audio/Main theme ZVEREV.wav")