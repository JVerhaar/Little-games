import pygame
import time
import random

pygame.init()#initiation function 

pygame.display.set_caption('Totem Carver')#screen, named Totem Carver
gameDisplay = pygame.display.set_mode((1280,720))#Makes the screen

blue = (100,149,237)
light_blue = (135,206,250)
alice_blue = (240, 248, 255)

def text_objects(text, font): #For text making purposes
    textSurface = font.render(text, True, alice_blue)
    return textSurface, textSurface.get_rect()



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

            #Button
            mouse = pygame.mouse.get_pos() #makes sure you can click on stuff
            if 493 + 250 > mouse[0] > 493 and 579 + 80 > mouse[1] > 579: #if the x coordinate + width  of the button = bigger than the 0 x position of the mouse than the x coordinate of the button(right side and same with left side)
                pygame.draw.rect(gameDisplay, light_blue, (493,579,250,80))#x, y, width, length
            else:
                pygame.draw.rect(gameDisplay, blue, (493,579,250,80))
            #Text on the button
            smallText = pygame.font.Font("freesansbold.ttf", 30)
            textSurf, textRect = text_objects("Play!", smallText)
            textRect.center = ((493 + (250 / 2)), (579 + (80 / 2))) #Put text in the center
            gameDisplay.blit(textSurf, textRect)

            pygame.display.update()#updates the screen?

#Runs the gamemenu   
gm = GameMenu(gameDisplay)
gm.run()