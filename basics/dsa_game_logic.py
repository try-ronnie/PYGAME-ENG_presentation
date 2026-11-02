import pygame 
# learning how to store items in lists and dictionaries ...
# for the english game we are gonna need to keep the answers and questions together
#initialize lib 

# add a question counter
current_question = 0 

questions = [
    {
        'question' : 'Kate went to the pet store to buy a ?',
        'options' : ['beach' , 'bitch'],
        'answer' : 'bitch',
    },
    {
        'question' : 'i need your ____ on this matter',
        'options' : ['advice' , 'advise'],
        'answer': 'advice'
    }
]
pygame.init()

#create surface 
DISPLAYSURF = pygame.display.set_mode ((1000,1000))

#common colour variables 
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,0,0)
black = (0,0,0)

