import pygame , sys


pygame.init() # initialize the programme 



# colour variables
red = (255, 0 ,0)
green = (0,255,0)
blue  = (0,0,255)
white = (255,255,255)

# screen surface
DISPLAYSURF = pygame.display.set_mode((800 , 600))
# caption
pygame.display.set_caption('trying out collide points')

running = True 

answer_rect = pygame.Rect(200,300,400,400) # pre-defined rectangle values

while running: 
    DISPLAYSURF.fill(white) # changes the screen to white
    
    pygame.draw.rect(DISPLAYSURF , red , answer_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and answer_rect.collidepoint(event.pos):
                print ("rectanlge has been clicked")
            if event.button == 1 and answer_rect.collidepoint(event.pos) == False:
                print("somewhere else is clicked ")
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.flip()
                
pygame.exit()
    