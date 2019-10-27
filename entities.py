import settings
import pygame
from loot import generate_weapon

class Base(object):
    def __init__(self,x,y,image):
        self.graphic = pygame.image.load(image)
        self.drops = []
        self.gold = 0
        self.health = 100
        self.damage = 20
        self.max_movement = 2
        self.max_jump = 32
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x,self.y,16,16)
        self.attack_frames = 0
        self.attack_every_frames = 180
    def findpath(self):
        return (self.x,self,y)
    def nextmove(self):
        goto = self.findpath()
    def move(self, dx, dy):
        if dx != 0:
            self.move_axis(dx,0)
        if dy != 0:
            self.move_axis(0,dy)
    def move_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in settings.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom
    def frame(self):
        if self.attack_frames != 0 :
            self.attack_frames += -1
    def attack(self):
        if self.attack_frames < 1:
            settings.player.health -= self.damage
            self.attack_frames =  self.attack_every_frames
    def on_death(self):
        settings.player.inv.add_loot(self.drops)
        settings.plyaer.gold += self.gold
        settings.ent_list.remove(self)
class Orc(Base):
    def __init__(self,x,y):
        super().__init__(x,y,"assets/0x72_DungeonTilesetII_v1.3/frames/orc_shaman_idle_anim_f0.png")
        settings.ent_list += [self]
        self.drops.append(generate_weapon(settings.player.xp))