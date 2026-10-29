import pygame ,sys
from pygame.locals import *  # this imports all pygame products

# initialize the programme
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800 , 600))
pygame.display.set_caption('ENGLIFICATION') # sets the window name to the desired caption 

running = True () # variable that holds the truth 

while running:
    for event in pygame.event.get():
        if event.type == 'QUIT':
            pygame.quit()# fully terminates the program,
            sys.exit()# fully exits it 
        else:
            pygame.display.update()