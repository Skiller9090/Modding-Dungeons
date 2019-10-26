import pygame
import os
import random
from player import Player
from blocks import Wall
import settings


def gen_sec(blocks):
    return " "*blocks
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

pygame.display.set_caption("Get to the red square!")

music = pygame.mixer.music.load("assets/music/type2.wav")

clock = pygame.time.Clock()
#walls = []
player = Player()
settings.init()

levelfile = open("level.txt","r")
level = levelfile.read().split("\n")
levelfile.close()

x = y = 0
def blank(x):
    return None
block_ids = {"0": blank,"1": Wall,"2": ""}
#block_lists = {0: None, 1: settings.walls}
for row in level:
    for col in row:
        block_ids[col]((x, y))
        x += 16
    y += 16
    x = 0
wall_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wall_left.png")
player_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wizzard_f_idle_anim_f0.png")

while settings.running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            settings.running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            settings.running = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        if settings.jumping == False and settings.on_ground == True:
            player.move(0, -2)
            settings.jumping_to_go = settings.max_jump
            settings.jumping = True
    if key[pygame.K_DOWN]:
        player.move(0, 2)
    if settings.jumping_to_go <= 0:
        player.move(0, 1)
    if settings.jumping_to_go > 0 and settings.jumping == True:
        settings.jumping_to_go -= 2
        player.move(0, -2)
    elif settings.on_ground == True and settings.jumping_to_go <= 0:
        settings.jumping = False
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
    settings.screen.fill((0, 0, 0))
  
    for wall in settings.walls:
        pygame.draw.rect(settings.screen, (255, 255, 255), wall.rect)
        settings.screen.blit(wall_graphic, wall.rect)
    pygame.draw.rect(settings.screen, (0, 0, 0), player.rect)
    settings.screen.blit(player_graphic,(player.rect[0],player.rect[1]-8))
    
    player.healthbar()

    pygame.display.flip()
