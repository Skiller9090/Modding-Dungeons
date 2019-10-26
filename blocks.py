import pygame


class Wall(object):
    def __init__(self, pos):
        self.id = 1
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
