import pygame
from settings.configuration import *

class Orcc(object):
    def __init__(self, game):
        self.game = game
        self.box = pygame.Rect(100, 100, 55, 25)

    def tick(self):
        pass

    def draw(self):
        pygame.draw.rect(screen, (0, 150, 120), self.box)