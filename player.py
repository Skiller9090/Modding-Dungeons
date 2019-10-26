import pygame
import init
from inventory import inventory

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(32,32,16,16)
        self.health = 100
        self.maxhealth = 100
        self.gold = 0
        self.inv = inventory()
    def move(self, dx, dy):
        if dx != 0:
            self.move_axis(dx,0)
        if dy != 0:
            self.move_axis(0,dy)

    def get_pos(self):
        return (self.rect.x, self.rect.y)

    def move_axis(self, dx, dy):
        global on_ground
        self.rect.x += dx
        self.rect.y += dy
        og = False
        for wall in init.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                    og = True
                if dy < 0:
                    self.rect.top = wall.rect.bottom
        if og == True:
            on_ground = True
        else:
            on_ground = False

        init.on_ground = og
