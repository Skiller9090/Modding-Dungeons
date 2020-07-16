import pygame

import settings
from inventory import inventory


class Player(object):
    def __init__(self, dataManager):
        self.dataManager = dataManager
        self.rect = pygame.Rect(self.dataManager.spawnpoint[0]*self.dataManager.block_size_x,
                       self.dataManager.spawnpoint[1]*self.dataManager.block_size_y, 16, 16)
        self.health = 100
        self.maxhealth = 100
        self.gold = 0
        self.inv = inventory()
        self.xp = 0
        self.level = 0

    def on_death(self):
        self.respawn()
        self.gold = 0
        self.health = self.maxhealth
        del self.inv
        self.inv = inventory

    def respawn(self):
        self.rect.x, self.rect.y = (self.dataManager.spawnpoint[0] * self.dataManager.block_size_x,
                                    self.dataManager.spawnpoint[1] * self.dataManager.block_size_y)

    def move(self, dx, dy):
        if dx != 0:
            self.move_axis(dx, 0)
        if dy != 0:
            self.move_axis(0, dy)

    def get_pos(self):
        return self.rect.x, self.rect.y

    def move_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        og = False
        for wall in self.dataManager.walls:
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
            self.dataManager.on_ground = True
        else:
            self.dataManager.on_ground = False
        for ent in self.dataManager.ent_list:
            if self.rect.colliderect(ent.rect):
                ent.attack()
                ent.on_death()

    def healthbar(self):
        pygame.draw.rect(self.dataManager.screen, (255, 0, 0), pygame.Rect(self.dataManager.sx - 100, 0, 100, 16))
        percent = self.health / self.maxhealth
        if percent > 1:
            percent = 1
        if percent < 0:
            percent = 0
        pygame.draw.rect(self.dataManager.screen, (0, 255, 0), pygame.Rect(self.dataManager.sx - 100, 0, percent * 100, 16))

    def display_gold(self):
        text = self.dataManager.font.render(("Gold: " + str(self.gold)), True, (232, 180, 48), (0, 0, 0, 0))
        textRect = text.get_rect()
        textRect.topright = (self.dataManager.sx, 16)
        self.dataManager.screen.blit(text, textRect)
