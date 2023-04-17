import pygame
from pygame.locals import *

# SCREEN SIZE
screen_size = (1920, 1080)
screen = pygame.display.set_mode(screen_size, HWSURFACE | DOUBLEBUF)

# Screen background
background = pygame.image.load('resources/bg.jpg').convert()
background = pygame.transform.smoothscale(background, screen.get_size())

# Basic settings
FPS_MAX = 144.0


