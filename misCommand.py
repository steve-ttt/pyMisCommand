import pygame
import sys
from pygame.locals import *

# Globals
WIDTH  = 800
HEIGHT = 600
EXPLSPEED = 2               #explosion speed

# Colour Constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
LBLUE = ( 98,   7, 250)
YELLOW =(255, 255,   0)

FPS = 30                    # frames per second setting
fpsClock = pygame.time.Clock()


pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Missile Command!')

# draw on the surface object
DISPLAYSURF.fill(BLACK)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

# Fonts
fontObj = pygame.font.Font('freesansbold.ttf', 10)
textSurfaceObj = fontObj.render('Coordinates: 0, 0', True, GREEN, BLACK)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (50, 10)

# images
catImg = pygame.image.load('cat.png')
bground = pygame.image.load('assets/bground.png')
catx = 10
caty = 10
direction = 'right'

explosions=[]  #[mousex, mousey, pygame.time.get_ticks(), 5, False] ie: x, y, time start, start size, max size reached true/false

# run the game loop
while True:
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(bground, (0,0))
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    
    
    # draw explosions from list
    for expl in explosions:
        pygame.draw.ellipse(DISPLAYSURF, RED, (expl[0], expl[1], expl[3], expl[3]), 1)
        if expl[3] <= 80 and expl[4] == False:
            expl[3] = expl[3] + EXPLSPEED
        elif expl[3] == 5 and expl[4] == True:
            explosions.remove(expl)
        else:
            expl[4] = True
            expl[3] = expl[3] - EXPLSPEED
    
    #Delete explosions from list if older than 3 sec
    #for expl in explosions:
    #   if expl[2] <= pygame.time.get_ticks() - 3000:
    #        explosions.remove(expl)
    
    
    # event handler
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            mouseStr = 'Coordinates: {latitude}, {longitude}'.format(latitude=mousex, longitude=mousey)
            textSurfaceObj = fontObj.render(mouseStr, True, GREEN, BLACK)
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            pygame.draw.line(DISPLAYSURF, YELLOW, (400,600), (mousex, mousey), 2)
            explosions.append([mousex, mousey, pygame.time.get_ticks(), 5, False])    #set X, y, and time of creation
            pygame.draw.ellipse(DISPLAYSURF, RED, (mousex - 40, mousey -20, 80, 40), 1)
            
    
    pygame.display.update()

    fpsClock.tick(FPS)


