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

def text_objects(text, font): #For text making purposes
    textSurface = font.render(text, True, alice_blue)
    return textSurface, textSurface.get_rect()

def Button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos() #makes sure you can click on stuff
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y: #if the x coordinate + width  of the button = bigger than the 0 x position of the mouse than the x coordinate of the button(right side and same with left side)
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))#
        
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
            
    #Text on the button
    smallText = pygame.font.Font("freesansbold.ttf", 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2))) #Put text in the center
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

class GameMenu(): #Game menu
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('D:/jessi/Documents/Totemcarver main/placeholder beginningscreen.png')#background start screen
       
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #Makes the screen
            gameDisplay.blit(self.background,(0,0,))

            Button("Play!", 493,579,250,80, blue, light_blue,game_loop)
            Button("Quit", 1210,650,50,50, red, bright_red,quitgame)
            
            pygame.display.update()#updates the screen?

def game_loop():
    game_bg = pygame.image.load('D:/jessi/Documents/Totemcarver main/Placeholder background game.png')
    gameDisplay.blit(game_bg, (0,0))
    pygame.display.update()

def Log(x, y):
    gameDisplay.blit('D:/jessi/Documents/Totemcarver main/Log.png')

def Carved_totem(x, y):
    gameDisplay.blit('D:/jessi/Documents/Totemcarver main/Empty totem.png')

def Dyed_totem(x,y):
    gameDisplay.blit('D:/jessi/Documents/Totemcarver main/Paint red totem.png')

def Totem(x,y):
    gameDisplay.blit('D:/jessi/Documents/Totemcarver main/Finished totem.png')



#Runs all the things!   
gm = GameMenu(gameDisplay)
gm.run()
game_loop()
pygame.quit()
quit()