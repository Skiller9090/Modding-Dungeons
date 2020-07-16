import os

import pygame

import keyboard
from settings import DataManager
from blocks import Wall
from entities import Orc
from pygame.locals import *


def gen_sec(blocks):
    return " " * blocks


os.environ["SDL_VIDEO_CENTERED"] = "0"
pygame.init()

dataManager = DataManager()

pygame.display.set_caption("Modding Dungeons")

music = pygame.mixer.music
loaded_music = music.load("assets/music/type2.wav")
music.set_volume(dataManager.volume)

clock = pygame.time.Clock()

levelfile = open("level.txt", "r")
level = levelfile.read().split("\n")
levelfile.close()


def blank(_, dm):
    return None


def Spawn(pos, dm):
    dm.spawnpoint = pos


block_ids = {"0": blank,
             "1": Wall,
             "2": Spawn}

for y, row in enumerate(level):
    for x, col in enumerate(row):
        block_ids[col]((x, y), dataManager)


wall_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wall_left.png")
dataManager.player_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wizzard_f_idle_anim_f0.png")
Orc(0, 0, dataManager)
dataManager.player.respawn()
while dataManager.running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            dataManager.running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            dataManager.running = False
        if e.type == pygame.VIDEORESIZE:
            # There's some code to add back window content here.
            dataManager.screen = pygame.display.set_mode((e.w, e.h), HWSURFACE | DOUBLEBUF | RESIZABLE)
            x_scale = e.w/dataManager.sx
            y_scale = e.h/dataManager.sy
            dataManager.block_size_x *= x_scale
            dataManager.block_size_y *= y_scale
            dataManager.sx = e.w
            dataManager.sy = e.h
            for wall in dataManager.walls:
                wall.calculate_scale()
            for entity in dataManager.ent_list:
                entity.calc_scale()

    keyboard.check(dataManager)
    if not music.get_busy() and dataManager.muted is not True:
        music.play()
    dataManager.screen.fill((0, 0, 0))

    for wall in dataManager.walls:
        dataManager.screen.blit(pygame.transform.scale(wall_graphic, (wall.rect.w, wall.rect.h)), wall.rect)

    dataManager.screen.blit(pygame.transform.scale(dataManager.player_graphic,
                                                   (int(dataManager.block_size_x), int(dataManager.block_size_y*2))),
                            (dataManager.player.rect[0], dataManager.player.rect[1]-dataManager.block_size_y))

    for ent in dataManager.ent_list:
        ent.move(0, 1)
        ent.frame()
        #for i in ent.drops:
            #print(i.damage, i.worth, i.name)
        dataManager.screen.blit(pygame.transform.scale(ent.graphic,
                                                       (int(dataManager.block_size_x), int(dataManager.block_size_y))),
                                (ent.rect[0], ent.rect[1]))

    dataManager.player.healthbar()
    dataManager.player.display_gold()

    pygame.display.flip()
