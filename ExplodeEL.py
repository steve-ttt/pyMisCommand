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
    def __init__(self, colour, width, height):
        """ Exploding elipse constructor, for use in missle command game
            Instantiate with colour, height and width """
        super(ExplodeEL,self).__init__()
        self.image = pygame.Surface([width, height] )
        self.image.fill(colour)
        #update the position of this object by setting the values of
        # rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        #called each frame
        #todo make it expand and contract
        #print('at update x: %s y: %s ' % (self.rect.x, self.rect.y))
        #self.rect.y += 1
        if self.rect.x <0 or self.rect.x > 800:
            print('killing sprite')
            self.kill()
        if self.rect.y < 0 or self.rect.y > 600:
            print('killing sprite')
            self.kill()
