import pygame

#initiaite 
pygame.init()

# create the display surface 
DISPLAYSURF = pygame.display.set_mode((1000,1000))

#creating a font
pygame.font.Font(None , 38)

# set common colour variables 
red = (255, 0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255, 255 ,0)
purple = (128,0,128)
white = (255,255,255)
#defining shapes to be used in the displaay
rect1 = pygame.Rect(200,400,200,200)
rect2 = pygame.Rect(400,400,200,200)
rect3 = pygame.Rect(600,400,200,200)

#creating text to be rendered in the rectangles
text1 = pygame.Font.render('answer a ' , True , green)
text1_rect = text1.get_rect(center = rect1.center) # create the sruface on the rect????
text2 = pygame.Font.render('answer b' , True , red)
text2_rect = text2.get_rect(center = rect2.center)
text3 = pygame.Font.render('answer c' , True , white)
text3_rect = text3.get_rect(center = rect3.center)
    

#setting the loop value 
running = True

while running:
    #fill screen to white
    DISPLAYSURF.fill(white)
    
    
    # draw the rectangles to surface
    r1= pygame.draw.rect(DISPLAYSURF , red , rect1)
    r2 = pygame.draw.rect(DISPLAYSURF, blue , rect2)
    r3 = pygame.draw.rect(DISPLAYSURF, green , rect3)
    r4 = pygame.draw.circle(DISPLAYSURF, yellow ,(100, 600), 50)
    

    for event in pygame.event:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if rect1.collidepoint(event.pos):
                    print('first rectangle clicked')
                if rect2.collidepoint(event.pos):
                    print('second rectangle clicked')
                if rect3.collidepoint(event.pos):
                    print('third rectangle clicked')
                else :
                    print('somewhere else clicked')
            if event.type == pygame.QUIT:
                running = False
    rect1.blit(text1_rect,)
    DISPLAYSURF.blit(text2 , (500,500))
    DISPLAYSURF.blit(text3 , (700,500))
    pygame.display.flip()
    
    