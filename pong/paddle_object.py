import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600

class paddle(object):

	def __init__(self,screen,x,y,length,width,player,speed):
		self.length = length
		self.width = width
		self.x = x
		self.y = y
		self.player = player
		self.screen = screen
		self.speed = speed

		

	def move(self):
		keys = pygame.key.get_pressed()

		if self.player == 'one':
			if keys[pygame.K_UP]:
				if self.y>=0:
					self.y -= self.speed
			if keys[pygame.K_DOWN]:
				if self.y+self.length<=HEIGHT:
					self.y += self.speed
		if self.player == 'two':
			if keys[pygame.K_w]:
				if self.y>=0:
					self.y -= self.speed
			if keys[pygame.K_s]:
				if self.y+self.length<=HEIGHT:
					self.y += self.speed

		pygame.draw.rect(self.screen,(255,255,255),[self.x,self.y,self.width,self.length])


		


		
		
			
