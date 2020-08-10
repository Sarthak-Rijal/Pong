import pygame
import numpy as np
from ball import *
from NN import * 
pygame.init()

WIDTH = 1000
HEIGHT = 600

MAXANGLE = math.pi/4
MAXSPEED = 15

#copied this form Arturs code. This sets up the normalized input for the input nodes

def prepare_features(ball_dx, ball_dy, y_ball, y_paddle):
	return np.array([ball_dy/MAXSPEED, ball_dx/MAXSPEED, (y_ball-y_paddle)/HEIGHT, y_paddle/HEIGHT])

class Paddle(object):
	
	def __init__(self, screen, length ,width, player, color, speed, mode = "default"):
		
		self._player = player

		if (self._player == "one"):
			self._posX = 950
			self._posY = HEIGHT / 2 - length/2
		else:
			self._posX = 25
			self._posY = HEIGHT / 2 - length/2
		
		self._screen = screen
		
		self._length = length
		self._width = width
		self._color = color
		self._player = player
		self._speed = speed
		self._mode = mode

		#defines a neural network with 4 inputs and 4 hidden nodes. 
		self._nn = NN(4, 4)

#To Do
####################################################################################################
		#need to make this so that the gene sequence determines these weights
		#	-how to map genes to weights?
		#  
		#initially random weights and biases
		self.A = np.random.rand(4,4) * 2 -1
		self.bias1 = np.random.rand(4, 1) * 2 - 1
		self.C = np.random.rand(1,4) * 2 - 1
		self.bias2 = np.random.rand(1, 1) * 2 - 1
######################################################################################################

		self.config = {'one': {'w': pygame.K_i, 's': pygame.K_k}, 'two': {'w':pygame.K_w, 's':pygame.K_s }}

		self._rect = pygame.Rect((self._posX, self._posY),(self._width, self._length))


	def _update(self, ball):

		if (self._player == "one"):
			self.move_kb()
		else:
			self.move_ai(ball)
		
		self._collide(ball)

		self._rect = pygame.Rect((self._posX, self._posY),(self._width, self._length))
		pygame.draw.rect(self._screen, self._color, (self._posX, self._posY, self._width, self._length))
		

	def _move_down(self,):

		if self._posY+self._length<=HEIGHT:
			self._posY += self._speed

	def _move_up(self):

		if self._posY >= 0:
			self._posY -= self._speed


	def _collide(self, ball):

		if (ball._rect.colliderect(self._rect)):
			
			#if its a training paddle it bounces randomly 
			if (self._mode == "train"):
				normalY = normalY = random.random()*2-1
			else:
			
			#if its a regular paddel it bounces depending where it lands on the paddle
				relativeY = -ball._posY - ball._size/2 + self._posY + self._length/2
				normalY = relativeY/(self._length/2)


			theta = MAXANGLE * normalY
			ball.bounce(theta, MAXSPEED, self._player)
			

	def move_kb(self):

		keys = pygame.key.get_pressed()

		if keys[self.config[self._player]['w']]:
			self._move_up()
		elif keys[self.config[self._player]['s']]:
			self._move_down()

	#basic format of the move AI
	#def prepare_features(ball_dx, ball_dy, y_ball, y_paddle):
    #return np.array([ball_dy/MAXSPEED, ball_dx/MAXSPEED, (y_ball-y_paddle)/HEIGHT, y_paddle/HEIGHT])
	def move_ai(self, ball):

		input = prepare_features(ball._velocityX, ball._velocityY, ball._posY, self._posY)		

		print(input)		
		decision = self._nn.neuralNetwork(self.A, self.bias1, self.C, self.bias2, input)
		if decision > 0.2:
			self._move_up()
		elif decision < -0.2:
			self._move_down()