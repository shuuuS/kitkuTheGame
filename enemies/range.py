import pygame

class Borc(object):
    def __init__(self, game):
        self.game = game
        self.box = pygame.Rect(250, 400, 45, 25)

    def tick(self):
        pass

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 255, 1), self.box)