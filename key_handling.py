import pygame


pygame.init()

DISPLAYSURF = pygame.display.set_mode((800 , 600))

running = True

while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                print('key down pressed')
            elif event.key == pygame.K_UP:
                print('Key up pressed')
            elif event.key == pygame.K_LEFT:
                print('key left is pressed')
            elif event.key == pygame.K_RIGHT:
                print('Key right is oressed')
    pygame.display.flip()
    
    
    # this is for key inputs note that 