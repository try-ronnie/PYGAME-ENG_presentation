# Simple english pygame prod1 :
This is a pygame dev project . Its a simple english game that teachers the user through his inputs which word are used depending on contecxt and common spelling errors.w



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
    
# #Every iteration of the while loop:
# 1. Checks for pending events.
# 2. Processes those events.
# 3. Updates game information.
# 4. Refreshes the display.
# 5. Starts another iteration.
# Here's the important distinction:

# The while loop repeats the entire game cycle.

# The for loop only processes the events waiting in the event queue.

# That's why we separate them.
# Let's make this practical
# Imagine your game has a cartoon character that changes its expression every time the player answers correctly.

# Even if the player doesn't touch anything, your game still needs to display the current character expression.

# If display updating were dependent on receiving an event, your rendering would be unnecessarily tied to user interaction.
# Mini challenge: Lesson 1 checkpoint
# Before Lesson 2, answer these three questions:
# 1. What would happen if we put running = False outside the if event.type == pygame.QUIT condition but inside the while loop?
# 2. What's the difference between the while loop and the for event loop?
# 3. If we draw a red rectangle onto the screen but never call pygame.display.flip(), what would happen to the visible display?
# Don't Google these. Reason them out.

# Then we'll tackle Lesson 2: