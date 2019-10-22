import pygame
import os
import random
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
        for wall in walls:
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

class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

def gen_sec(blocks):
    return " "*blocks
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
sx = 640
sy = 480
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((sx, sy))


clock = pygame.time.Clock()
walls = []
player = Player()

levelfile = open("level.txt","r")
level = levelfile.read().split("\n")
levelfile.close()
def healthbar():
    pygame.draw.rect(screen, (255, 0, 0),pygame.Rect(sx-100,0,100,16))
    percent = player.health/player.maxhealth
    if percent > 1:
        percent = 1
    if percent < 0:
        percent = 0
    pygame.draw.rect(screen, (0, 255, 0),pygame.Rect(sx-100,0,percent*100,16))    
x = y = 0
def blank():
    None
block_ids = {"0": blank,"1": Wall,"2": ""}
for row in level:
    for col in row:
        block_ids[col]((x, y))
        x += 16
    y += 16
    x = 0
wall_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wall_left.png")
player_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wizzard_f_idle_anim_f0.png")
running = True
jumping = False
jumping_to_go = 0
max_jump = 32
on_ground = False
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        if jumping == False and on_ground == True:
            player.move(0, -2)
            jumping_to_go = max_jump
            jumping = True
    if key[pygame.K_DOWN]:
        player.move(0, 2)
    if jumping_to_go <= 0:
        player.move(0, 1)
    if jumping_to_go > 0 and jumping == True:
        jumping_to_go -= 2
        player.move(0, -2)
    elif on_ground == True and jumping_to_go <= 0:
        jumping = False


    screen.fill((0, 0, 0))
  
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        screen.blit(wall_graphic, wall.rect)
    pygame.draw.rect(screen, (0, 0, 0), player.rect)
    screen.blit(player_graphic,(player.rect[0],player.rect[1]-8))
    
    healthbar()

    pygame.display.flip()
