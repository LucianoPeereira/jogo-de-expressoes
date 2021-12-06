import pygame
from pygame import mixer

pygame.mixer.init()

class Sounds():

    def __init__(self, botao = ""):
        self.botao = botao

    def menu(self, active):
        if active == True:
            self.botao = pygame.mixer.Sound("utils/music/goup.wav")
            self.botao.play()

    def voltar(self, active):
        if active == True:
            self.botao = pygame.mixer.Sound("utils/music/godown.wav")
            self.botao.play()

    def gameOver(self, active):
         if active == True:
            self.botao = pygame.mixer.Sound("utils/music/Crowd.ogg")
            self.botao.play()

    def expcorreta(self, active):
         if active == True:
            self.botao = pygame.mixer.Sound('utils/music/stop.wav')
            self.botao.play()

    def clock(self, active):
         if active == True:
            self.botao = pygame.mixer.Sound("utils/music/clock.wav")
            self.botao.play()

    def clocknot(self):
        #     botao = pygame.mixer.Sound("music/clock.wav")
            self.botao.stop()


