import pygame, sys
from pygame.locals import *

from characters.poripori import Poripori
from enemies.melee import Orcc
from enemies.range import Borc

from settings.configuration import *


class Game(object):
    def __init__(self):
        
        # Initialization
        pygame.init()
        
        # Import classes
        self.player = Poripori(self)
        self.meleeOrc = Orcc(self)
        self.bowOrc = Borc(self)

        # Ticking
        self.fps_clock = pygame.time.Clock()
        self.const_delta = 0.0

        
        
        while True:

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.FPS_MAX = FPS_MAX
            self.const_delta += self.fps_clock.tick() / 1000.0
            while self.const_delta > 1 / self.FPS_MAX:
                self.tick()
                self.const_delta -= 1 / self.FPS_MAX
                

            # Rendering
            screen.fill((0, 0, 0))
            self.draw()
            screen.blit(background, (0, 0))

            pygame.display.flip()

            
    def tick(self):
       self.player.tick()
       
    def draw(self):
        self.player.draw()
        # self.meleeOrc.draw()
        # self.bowOrc.draw()
        
if __name__ == "__main__":
    Game()





