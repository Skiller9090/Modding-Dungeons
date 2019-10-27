import pygame
from inventory import inventory
import settings

class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(32,32,16,16)
        self.health = 100
        self.maxhealth = 100
        self.gold = 0
        self.inv = inventory()
        self.xp = 0
        self.level = 0
    def move(self, dx, dy):
        if dx != 0:
            self.move_axis(dx,0)
        if dy != 0:
            self.move_axis(0,dy)

    def get_pos(self):
        return (self.rect.x, self.rect.y)

    def move_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        og = False
        for wall in settings.walls:
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
            settings.on_ground = True
        else:
            settings.on_ground = False
        for ent in settings.ent_list:
            if self.rect.colliderect(ent.rect):
                ent.attack()
    def healthbar(self):
        pygame.draw.rect(settings.screen, (255, 0, 0),pygame.Rect(settings.sx-100,0,100,16))
        percent = self.health/self.maxhealth
        if percent > 1:
            percent = 1
        if percent < 0:
            percent = 0
        pygame.draw.rect(settings.screen, (0, 255, 0),pygame.Rect(settings.sx-100,0,percent*100,16))    