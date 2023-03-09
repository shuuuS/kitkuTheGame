import pygame

class Poripori(object):
    def __init__(self, game):
        self.game = game
        self.box = pygame.Rect(500, 500, 100, 25)

    def tick(self):
        pass

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 150, 255), self.box)