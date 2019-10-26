import pygame
import settings

class Wall(object):
    def __init__(self, pos):
        self.id = 1
        settings.walls += [self]
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
