import pygame, sys
from characters.poripori import Poripori

class Game(object):
    def __init__(self):
        # Config
        self.tps_max = 144.0
        self.movement_speed = 1
        

        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720)) # screen size

        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player = Poripori(self)

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking
            self.tps_delta += self.tps_clock.tick()/1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max
            
            # Rendering
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
       self.player.tick()

    def draw(self):
        self.player.draw()
        

if __name__ == "__main__":
    Game()





