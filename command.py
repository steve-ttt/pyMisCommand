#!/usr/bin/env python2

import pygame
import random
import sys
import spritesheet
from pygame.locals import *
from ExplodeEL import ExplodeEL

WIDTH = 800
HEIGHT = 600
FPS = 30

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



## initialize pygame and create window

pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missile Command")
clock = pygame.time.Clock()     ## For syncing the FPS
bground = pygame.image.load('assets/bground.png')

## draw some text
# Fonts
fontObj = pygame.font.Font('freesansbold.ttf', 10)
textSurfaceObj = fontObj.render('Coordinates: 0, 0', True, GREEN, BLACK)
textCoord = textSurfaceObj.get_rect()
textCoord.center = (50, 10)

## group all the sprites together for ease of update
all_sprites = pygame.sprite.Group()
explosions = pygame.sprite.Group()


## Game loop
running = True
while running:

    #1 Process input/events

    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            mouseStr = 'Coordinates: {mx}, {my}'.format(mx=mousex, my=mousey)
            textSurfaceObj = fontObj.render(mouseStr, True, GREEN, BLACK)
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            new_expl = ExplodeEL(RED, 80, 40)
            new_expl.rect.x = mousex
            new_expl.rect.y = mousey
            explosions.add(new_expl)
            all_sprites.add(new_expl)


    #2 Update
    all_sprites.update()


    #3 Draw/render
    screen.fill(BLACK)
    screen.blit(bground, (0,0))
    screen.blit(textSurfaceObj, textCoord)
    #explosions.draw(screen)
    all_sprites.draw(screen)


    ## Done after drawing everything to the screen
    pygame.display.flip()
    clock.tick(FPS)     ## will make the loop run at the same speed all the time

pygame.quit()
