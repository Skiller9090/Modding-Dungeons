import settings
import pygame

def check():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        settings.player.move(-2, 0)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
        settings.player.move(2, 0)
    if key[pygame.K_UP] or key[pygame.K_w]:
        if settings.jumping == False and settings.on_ground == True:
            settings.player.move(0, -2)
            settings.jumping_to_go = settings.max_jump
            settings.jumping = True
    if key[pygame.K_DOWN] or key[pygame.K_s]:
        settings.player.move(0, 2)
    if settings.jumping_to_go <= 0:
        settings.player.move(0, 1)
    if settings.jumping_to_go > 0 and settings.jumping == True:
        settings.jumping_to_go -= 2
        settings.player.move(0, -2)
    elif settings.on_ground == True and settings.jumping_to_go <= 0:
        settings.jumping = False