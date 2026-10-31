import pygame , sys

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800 , 600))


running = True

answer_rect = pygame.rect(100 , 200 ,100 , 100) # pygame.rect (starting x-axis , y-axis , width , height)
# this means the rect angle starts at x-axis = 100 and y-axis = 200  , width of 100 px , height of 100 pixels

# rectangles have special functions --- collidepoint()
    # checks whether a particular point falls into the rectangle
    # it expects a tuple of a position given
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print('key down presed')
        