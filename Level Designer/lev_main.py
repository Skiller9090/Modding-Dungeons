#!/usr/bin/python3
import pygame

pygame.init()

sx = 1000
sy = 1000

screen = pygame.display.set_mode((sx, sy))
clock = pygame.time.Clock()

wall_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wall_left.png")
char_grpahic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/wizzard_f_idle_anim_f0.png")
ches_graphic = pygame.image.load("assets/0x72_DungeonTilesetII_v1.3/frames/chest_full_open_anim_f0.png")

running = True

class block(object):
    def __init__(self, pos):
        self.id = 0
        row_list.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

def convert_to_file():
    d3_matrix = []
    for row in block_grid:
        string = ""
        for block in row:
            string += str(block.id)
        d3_matrix.append(string)
    ffile = open("level.txt","w")
    ffile.write("\n".join(d3_matrix))
    ffile.close()
    print(string)
cx = 640
cy = 480
block_grid = []
w = int(cx/16)
h = int(cy/16)
for row in range(h):
    row_list = []
    for col in range(w):
        block((col*16,row*16))
    block_grid.append(row_list)
convert_rect = pygame.Rect(cx+20, 0, 16, 16)
while running:
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                for row in block_grid:
                    for block in row:            
                        if block.rect.collidepoint(e.pos):
                            block.id = 1
            if e.button == 1:
                if convert_rect.collidepoint(e.pos):
                    convert_to_file()

    screen.fill((0, 0, 0))
    for row in block_grid:
        for block in row:
            pygame.draw.rect(screen, (255, 255, 255),  block.rect)
            if block.id == 1:
                screen.blit(wall_graphic, block.rect)
    pygame.draw.rect(screen, (255, 0, 255), convert_rect)
    pygame.display.flip()
