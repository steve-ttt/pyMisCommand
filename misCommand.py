import pygame
import sys
from pygame.locals import *

# Globals
WIDTH  = 800
HEIGHT = 600

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hello World!')

# Colour Constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
LBLUE = ( 98,   7, 250)

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()


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
catx = 10
caty = 10
direction = 'right'

explosions=[]

# run the game loop
while True:
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    DISPLAYSURF.blit(catImg, (catx, caty))
    
    
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
         caty -= 5
         if caty == 10:
             direction = 'right'
    
    # draw explosions from list
    for expl in explosions:
        pygame.draw.ellipse(DISPLAYSURF, RED, (expl[0], expl[1], 10, 10), 1)
    
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
            pygame.draw.line(DISPLAYSURF, LBLUE, (400,600), (mousex, mousey))
            explosions.append([mousex, mousey])
            pygame.draw.ellipse(DISPLAYSURF, RED, (mousex - 20, mousey -40, 40, 80), 1)
    
    pygame.display.update()

    fpsClock.tick(FPS)


