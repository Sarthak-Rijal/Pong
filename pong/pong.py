import pygame,sys
pygame.init()


WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))





clock = pygame.time.Clock()
FPS = 60

bounce = False

#audio 
one_sound = pygame.mixer.Sound("sound/one.wav")
two_sound = pygame.mixer.Sound("sound/two.wav")

one_score = pygame.mixer.Sound("sound/one_score.wav")
two_score = pygame.mixer.Sound("sound/two_score.wav")

#sounds are alreay initilized. To play a sound simply do:

#  variable.play()


#Prints the desired "msg" (A string) of (int) "size" with int color as a rgb value (0-255,0-255,0-255) 
# anywhere in the window specfied by (int) x and (int) y
def print_f(msg,siz,color,x,y):
    Text = pygame.font.Font("freesansbold.ttf",siz)
    write = Text.render(msg,True,color)
    write_rect = write.get_rect()
    write_rect.center = ((x),(y))
    screen.blit(write,write_rect)

#Given a name of the player (String), displays the end screen
def win(player):
    color1 =  (100, 100, 100)
    color2 =  ( 60,  60, 100)
    for i in range(13):
        color1, color2 = color2, color1
        screen.fill(color1)
        print_f(player+" Won!!",32,(255,0,0),WIDTH/2,HEIGHT/2)
        pygame.display.update()
        pygame.time.wait(300)
    play()

#Implement this to reset the game after one player has scored. 


#def reset(x,bool): 
	

	


#skeleton code to fill in. This is the main loop where everything runs. 

def play():
	
	#event
	while True:
		

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		
		screen.fill((0,0,0))

		#draw stripes
		for i in range(HEIGHT):
			if i%25 == 0:
				pygame.draw.rect(screen,(255,255,255),(WIDTH/2-2,i,4,10))
	





		clock.tick(FPS)
		pygame.display.update()

play()