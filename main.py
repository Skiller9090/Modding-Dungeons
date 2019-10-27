import pygame
from pygame.locals import *
import os
import random
from blocks import Wall
import settings
from entities import Orc
import keyboard

def gen_sec(blocks):
    return " "*blocks
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

pygame.display.set_caption("Get to the red square!")

music = pygame.mixer.music.load("assets/music/type2.wav")

clock = pygame.time.Clock()

settings.init()

levelfile = open("level.txt","r")
level = levelfile.read().split("\n")
levelfile.close()
x = y = 0
def blank(x):
    return None
block_ids = {"0": blank,"1": Wall,"2": ""}

for row in level:
    for col in row:
        block_ids[col]((x, y))
        x += 16
    y += 16
    x = 0
wall_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wall_left.png")
settings.player_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wizzard_f_idle_anim_f0.png")
Orc(0,0)
while settings.running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            settings.running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            settings.running = False
    keyboard.check()
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
    settings.screen.fill((0, 0, 0))
  
    for wall in settings.walls:
        settings.screen.blit(wall_graphic, wall.rect)
    settings.screen.blit(settings.player_graphic,(settings.player.rect[0],settings.player.rect[1]-8))
    
    for ent in settings.ent_list:
        ent.move(0,1)
        ent.frame()
        for i in ent.drops:
            print(i.damage,i.worth,i.name)
        settings.screen.blit(ent.graphic,(ent.rect[0],ent.rect[1]))
    
    settings.player.healthbar()

    pygame.display.flip()
