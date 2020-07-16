import pygame
from pygame.locals import *

from player import Player


class DataManager:
    def __init__(self):
        self.walls = []
        self.running = True
        self.jumping = False
        self.jumping_to_go = 0
        self.max_jump = 32
        self.on_ground = False
        self.sx = 640
        self.sy = 480
        self.screen = pygame.display.set_mode((self.sx, self.sy), HWSURFACE | DOUBLEBUF | RESIZABLE)
        self.ent_list = []
        self.font = pygame.font.Font(None, 26)
        self.muted = False
        self.volume = 0.1
        self.block_size_x = 16
        self.block_size_y = 16
        self.blocks_row_size = 30
        self.blocks_column_size = 40
        self.spawnpoint = (0, 0)
        self.player = Player(self)
