import pygame
import sys
import spritesheet
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class ExplodeEL(pygame.sprite.Sprite):
    implode = False
    startw = 8
    starth = 4
    def __init__(self):
        """ Exploding elipse constructor, for use in missle command game
            Instantiate with colour, height and width """
        super(ExplodeEL,self).__init__()
        self.image = pygame.image.load("assets/exp.png").convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        #called each frame
        if self.implode == False:
            self.startw += 2
            self.starth += 2
            self.image = pygame.image.load("assets/exp.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(self.startw,self.starth))
        if self.startw >= 80:
            self.implode = True
        if self.implode == True:
            self.startw -= 2
            self.starth -= 2
            self.image = pygame.image.load("assets/exp.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,(self.startw,self.starth))
        if self.startw <= 4:
            self.kill()
