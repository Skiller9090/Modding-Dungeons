import pygame

def init():
    global walls
    global running
    global jumping
    global jumping_to_go
    global on_ground
    global max_jump
    global screen
    global sx
    global sy
    walls = []
    running = True
    jumping = False
    jumping_to_go = 0
    max_jump = 32
    on_ground = False
    sx = 640
    sy = 480
    screen = pygame.display.set_mode((sx, sy))