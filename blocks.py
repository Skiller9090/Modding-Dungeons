import pygame


class Wall(object):
    def __init__(self, pos, dataManager):
        self.dataManager = dataManager
        self.id = 1
        self.row = pos[1]
        self.column = pos[0]
        self.dataManager.walls += [self]
        self.rect =pygame.Rect(self.column*self.dataManager.block_size_x, self.row*self.dataManager.block_size_y,
                               self.dataManager.block_size_x, self.dataManager.block_size_y)

    def calculate_scale(self):
        self.rect = pygame.Rect(self.column*self.dataManager.block_size_x, self.row*self.dataManager.block_size_y,
                                self.dataManager.block_size_x, self.dataManager.block_size_y)