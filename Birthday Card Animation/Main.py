import pygame
import time
#Initialising pygame
pygame.init()

#Set up display
screen = pygame.display.set_mode((600,600))

#set the caption
pygame.display.set_caption("Happy Birthday")

#Load the images
load1 = pygame.image.load("images/image1.jpg")
load2 = pygame.image.load("images/image2.jpg")
load3 = pygame.image.load("images/image3.jpg")

#Scale the images
scale1 = pygame.transform.scale(load1,(600,600))
scale2 = pygame.transform.scale(load2,(600,600))
scale3 = pygame.transform.scale(load3,(600,600))

#converting the text to image
font = pygame.font.SysFont("Arial",70)
Htext = font.render("Happy Birthday", True,"Blue")



#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("White")
    screen.blit(scale1,(0,0))
    screen.blit(Htext,(15,15))

    
    #update the game
    pygame.display.update()

    time.sleep(2)


pygame.quit()