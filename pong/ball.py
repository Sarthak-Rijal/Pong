import pygame
import math

pygame.init()

#screen window
WIDTH = 1000
HEIGHT = 600



class Ball(object):
    
    
    def __init__(self, velocityX, velocityY, size, angle, speed, color):
        
        self._posX = WIDTH/2 - size/2
        self._posY = HEIGHT/2 - size/2

        self._velocityX = velocityX
        self._velocityY = velocityY
        self._angle = angle
        self._speed = speed
        self._size = size
        self._color = color

        self._rect = pygame.Rect((self._posX, self._posY),(self._size, self._size))
    
    
    def _update(self, surface):
        print (self._posX, self._posY, self._velocityX)
        self._collide()

        self._posX +=  self._velocityX
        self._posY +=  self._velocityY

        pygame.draw.rect(surface, self._color, [self._posX, self._posY, self._size, self._size])

    def _collide(self):
        
        if (self._posX + self._size > WIDTH or self._posX < 0):
            
            self._velocityX = -self._velocityX
            print ("Collide")
        
        if (self._posY + self._size > HEIGHT or self._posY < 0):
            self._velocityY = -self._velocityY

            print ("Collide")
        







#bounce function will tell how the ball will bounce	
#	def bounce(self):
	


# collide function will handle how the ball handel collisions
# 3 different cases:
#	1 - Ball bounces on the upper or lower ceiling
#	2 - Ball bounces on the paddle
#	3 - Ball bounces on the left or right end of the scree. 

#	def collide(self):

#	def update(self)


		


