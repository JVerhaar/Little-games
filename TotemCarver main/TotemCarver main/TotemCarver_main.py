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

def Button(msg, x, y, w, h, ic, ac, fs, action=None, action2=None):
    mouse = pygame.mouse.get_pos() #makes sure you can click on stuff
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y: #if the x coordinate + width  of the button = bigger than the 0 x position of the mouse than the x coordinate of the button(right side and same with left side)
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        
        if click[0] == 1 and action2 != None:
            action2()
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
            
    #Text on the button
    smallText = pygame.font.Font("freesansbold.ttf", fs)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2))) #Put text in the center
    gameDisplay.blit(textSurf, textRect)

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

            Button("Play!", 493,579,250,80, blue, light_blue, 30, new_screen, game_loop)
            Button("Quit", 1210,650,50,50, red, bright_red, 10, quitgame, None)
            
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
    pygame.display.update()

#Runs all the things!   
gm = GameMenu(gameDisplay)
gm.run()
game_loop()
pygame.quit()
quit()
new_screen()