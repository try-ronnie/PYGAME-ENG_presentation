import pygame ,sys

# initialize the programme
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800 , 600))
pygame.display.set_caption('ENGLIFICATION') # sets the window name to the desired caption 

running = True  # variable that holds the truth 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running =  False  #this is simpler since it will exit the loop
    pygame.display.flip()
    
