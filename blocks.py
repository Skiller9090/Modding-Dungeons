import pygame
import init

class Wall(object):
    def __init__(self, pos):
        init.walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
