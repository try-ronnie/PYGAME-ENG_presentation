import pygame

#initiaite 
pygame.init()

# create the display surface 
DISPLAYSURF = pygame.display.set_mode((800,800))

# set common colour variables 
red = (255, 0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255, 255 ,0)
purple = (128,0,128)
white = (255,255,255)
#defining shapes to be used in the displaay
rect1 = pygame.rect(200,400,100,100)
rect2 = pygame.rect(400,400,100,100)
rect3 = pygame.rect(600,400,100,100)

#setting the loop value 
running = True

while running:
    #fill screen to white
    DISPLAYSURF.fill(white)
    pygame.draw.rect(DISPLAYSURF , red , rect1)
    pygame.draw.rect(DISPLAYSURF, blue , rect2)