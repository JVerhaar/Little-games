import pygame

pygame.init()#initiation function 

pygame.display.set_caption('Totem Carver')#screen, named Totem Carver
gameDisplay = pygame.display.set_mode((1280,720))#Makes the screen

class GameMenu():
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('D:/jessi/Documents/Totemcarver main/placeholder beginningscreen.png')#background start screen
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            #Limit frame speed to 50FPS
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #Makes the screen
            gameDisplay.blit(self.background,(0,0))
            pygame.display.flip()


#Runs the gamemenu   
gm = GameMenu(gameDisplay)
gm.run()