import pygame
import os
import body
from body import Grid

os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 1920, 1080 #My screen size
size = (width, height)

pygame.init()
pygame.display.set_caption(" Game of life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
darkgrey = (169, 169, 169)
white = (220, 220, 220)
#

scaler = 20
offset = 1

Grid = body.Grid(width, height, scaler, offset)
Grid.random2d_array()


run = True
while run:
    clock.tick(fps)
    screen.fill(darkgrey)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Grid.Conway(off_color = black, on_color = white, surface=screen)
    pygame.display.update()

pygame.quit()