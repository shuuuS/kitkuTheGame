import pygame
from pygame.math import Vector2
import math
from settings.configuration import *

class Poripori(object):
    def __init__(self, game):
        
        # Initialization
        self.game = game
        size = screen.get_size()


        # Configuration
        self.position = Vector2(size[0]/2, size[1]/2)
        self.vel = Vector2(0, 0)
        self.acceration = Vector2(0, 0)
        self.movement_speed = 1

        self.image = pygame.image.load("resources/poripori.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        
    def image_follow_mouse_position(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.vel.x, mouse_y - self.vel.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.image, int(angle))
        self.rect = self.image.get_rect(center=self.position)

    def add_force(self, force):
        self.acceration += force
        # Physics
        self.vel *= 0.8
        self.vel += self.acceration
        self.position += self.vel
        self.acceration *= 0

    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force(Vector2(0, -self.movement_speed))
        if pressed[pygame.K_s]:
            self.add_force(Vector2(0, self.movement_speed))
        if pressed[pygame.K_a]:
            self.add_force(Vector2(-self.movement_speed, 0))
        if pressed[pygame.K_d]:
            self.add_force(Vector2(self.movement_speed, 0))
        

    def draw(self):
        screen.blit(self.image, (self.vel.x, self.vel.y))