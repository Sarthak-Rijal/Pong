import pygame
from paddle_object import paddle

pygame.init()

WIDTH = 1000
HEIGHT = 600


class Ball(object):
	
	def __init__(self, screen,x,y,size,x_speed,y_speed):
		
		self.screen = screen
		self.x = x
		self.y = y
		self.size = size
		self.x_speed = x_speed
		self.y_speed = y_speed

	def move(self):
		self.x+=self.x_speed
		self.y+=self.y_speed

		if (self.y <= 0 or self.y+self.size >= HEIGHT):
	
			self.y_speed = -self.y_speed




		pygame.draw.rect(self.screen,(255,255,255),[self.x,self.y,self.size,self.size])

	
	def bounce(self,ball_v,padd):
		if (ball_v >=0 and ball_v<=20):
			if padd == "one":
				self.x_speed = -7
				self.y_speed = -10
			if padd == "two":
				self.x_speed = 7
				self.y_speed = -10

		if (ball_v > 20 and ball_v<=40):
			if padd == "one":
				self.x_speed = -6
				self.y_speed = -6
			if padd == "two":
				self.x_speed = 6
				self.y_speed = -6

		if (ball_v > 40 and ball_v<=50):
			if padd == "one":
				if ball_v == 50:
					self.x_speed = -5
					self.y_speed = 0
				else:
					self.x_speed = -5
					self.y_speed = -1
			if padd == "two":
				if ball_v == 50:
					self.x_speed = 5
					self.y_speed = 0
				else:
					self.x_speed = 5
					self.y_speed = -1
		if (ball_v > 50 and ball_v<=60):
			if padd == "one":
				self.x_speed = -6
				self.y_speed = 6
			if padd == "two":
				self.x_speed = 6
				self.y_speed = 6

		if (ball_v > 60 and ball_v<=80):
			if padd == "one":
				self.x_speed = -5
				self.y_speed = 5
			if padd == "two":
				self.x_speed = 5
				self.y_speed = 5

		if (ball_v > 80 and ball_v<=100):
			if padd == "one":
				self.x_speed = -7
				self.y_speed = 10
			if padd == "two":
				self.x_speed = 7
				self.y_speed = 10



	def collide(self,other):
		return other.colliderect(pygame.Rect(self.x,self.y,self.size,self.size))


