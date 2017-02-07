import pygame
import time
import random

pygame.init()#initiation function 

display_width = 1280
display_height = 720

pygame.display.set_caption('Totem Carver')#screen, named Totem Carver
gameDisplay = pygame.display.set_mode((display_width, display_height))#Makes the screen

blue = (100,149,237)
light_blue = (135,206,250)
alice_blue = (240, 248, 255)
red = (200,0,0)
bright_red = (255,0,0)
background_image = pygame.image.load('images//Placeholder background game 2.png')

def text_objects(text, font): #For text making purposes
    textSurface = font.render(text, True, alice_blue)
    return textSurface, textSurface.get_rect()

class button:
	def __init__(self, msg, x, y, w, h, fs, action=None, action2 = None):
		self.msg = msg
		self.X = x
		self.Y = y
		self.Width = w
		self.Height = h
		self.IColor = (50,50,50)
		self.AColor = (100,100,100)
		self.FontSize = fs 
		self.Pressed = False
	
	def Hover(self):
		if self.X < pygame.mouse.get_pos()[0] < self.X + self.Width:
			if self.Y < pygame.mouse.get_pos()[1] < self.Y + self.Height:
				return True
		return False
	
	def draw(self):#methods hebben altijd self nodig
		if not self.Hover():
			pygame.draw.rect(gameDisplay, self.IColor, (self.X, self.Y, self.Width, self.Height))
		else:
			pygame.draw.rect(gameDisplay, self.AColor, (self.X, self.Y, self.Width, self.Height))

		

def quitgame():
    pygame.quit()
    quit()

class GameMenu(): #Game menu
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('images//placeholder beginningscreen.png')#background start screen
       
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            #Makes the screen
            gameDisplay.blit(self.background,(0,0,))
            Button_Play.draw()
           
            pygame.display.update()#updates the screen?

def new_screen():
    size = (display_width, display_height)
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.blit(background_image, [0,0])

    pygame.display.flip()
    pygame.display.update()


def game_loop():
    game_bg = background_image

    gameExit = False

    gameDisplay.blit(game_bg, (0,0))
    Button_Play.draw()
    pygame.display.update()

#Runs all the things!  
Button_Play = button("Play!",10,10,100,50,30) 
gm = GameMenu(gameDisplay)
gm.run()
game_loop()
pygame.quit()
quit()
new_screen()