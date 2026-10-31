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
# Don't Google these. Reason the# #Every iteration of the while loop:
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

# Then we'll tackle Lesson 2: Events, keyboard input and mouse input. This is where your quiz starts becoming interactive.m out.

# Then we'll tackle Lesson 2:




master :
    1.hnandle input 
    2.update game info
    3.draw everything >>> display flip
    4.refresh display




events ===is handling inputs from keys and using a mouse 

THERE ARE TWO TYPES OF MAIN EVENTS THATS MOUSEBUTTOWN DOWN AND KEYSDOWN
        1.after using the loop to get events occuring on surface .... we use
        2. event.type can either be : KEYDOWN (pressing of keys ) or MOUSEBUTTONDOWN

THEN TO GET TEH SPECIFIC KEY TYPES TO BE USED we thn use #event.key 
BUT TO GET THE MOUSE BUTTON CLICKED WE THEN USE : event_button

for event.key -- K_DOWN , K_UP , K_LEFT , K_RIGHT 

for event.button --  1(left click) , 2 (middle click) , 3(right click) , 4(scroll wheel up)  5, (scroll wheel down)


but then remember that thats only the keys for the mouse what about the mouse position..... pygame then privides us with >>> event.pos



DRAWING SURFACES 
when drawing it is good to keep the values of the surfaces to be drawn outside the loop for easier referencing 

so rectancle = pygame.rect(x-axis , y-axis , width , height)
        >> note : width == 0   .... leads to filling the rect
        >> note : width > 0 used for line thickness
        >> note : width < 0 draws nothing

drawing polygons : pygame.polygons(screen , colour , points , width)
drawing circles : pygame.draw.circle(screen , colour , (x-axis , y-axis ) , radius)
drawing lines : pygame.draw.line(screen , colour , staring_point , ending_point)
etc 



rendering text messages

we need to make a font :
>>>> pygame.font.Font(type of font , size)
>>>> type of font is passsed as a file string ..... no native pygame fonts
>>>this creates the font that will be used for any text wanting to be rendered

rendering the text:
    text = font.render('*desired text*' , antialiasing(input boolean) , colour)
    this creates a new surface rendering the text
    but the text is rendered into text format now we need to find a method to place it in the screen