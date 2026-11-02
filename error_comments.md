# error.py — Extracted Comments

All comments below are taken directly from `error.py`. No code was changed or removed from the original file.

---

## QUESTIONS THAT RUN THE GAME

```
# QUESTIONS THAT RUN THE GAME
# This is a list containing dictionaries.
# Each dictionary represents one question in our game.
#
# Every question has:
# q_no       = The question number.
# question   = The actual sentence/question displayed to the player.
# options    = A list containing the three possible answers.
# answer     = The correct answer against which the player's choice is checked.
# explanation = The explanation that will eventually be displayed after answering.
```

---

## ADDITIONAL VARIABLES

```
# ADDITIONAL VARIABLES
# These variables control the overall progress and state of the game.

# This keeps track of the question currently being displayed.
# Python starts counting list positions from zero.
# Therefore, current_question = 0 means we are displaying the first question.

# This variable stores the player's total score.
# Every time the player selects a correct answer, we increase this value by one.

# This stores the index of the option currently selected by the player.
# Our three buttons have indexes 0, 1 and 2.
# We use -1 to indicate that the player has not selected anything yet.
# This prevents the first button from automatically being highlighted gold.

# This variable tracks whether the player has submitted an answer to the current question.
# False means the question has not been answered yet.
# True means the player has already submitted an answer.
# This prevents the player from repeatedly pressing ENTER and increasing their score
# multiple times for the same question.
```

---

## SCREEN MEASUREMENTS

```
# SCREEN MEASUREMENTS
# These variables define the width and height of our Pygame display.
# Keeping the measurements in variables makes it easier to adjust the screen later.
```

---

## INITIALIZE THE LIBRARY

```
# INITIALIZE THE LIBRARY
# pygame.init() initializes the Pygame modules that we need.
# This must be called before creating our display, fonts and other Pygame objects.
```

---

## CREATE THE DISPLAY SURFACE

```
# CREATE THE DISPLAY SURFACE
# set_mode() creates the actual game window.
# We pass our screen width and height as a tuple.
# DISPLAYSURF is the surface on which we will draw everything in the game.

# This sets the name displayed at the top of the game window.
```

---

## CREATE THE REQUIRED COLOUR VARIABLES

```
# CREATE THE REQUIRED COLOUR VARIABLES
# Pygame represents colours using RGB values.
# RGB stands for Red, Green and Blue.
# Each colour component normally has a value between 0 and 255.
```

---

## CREATE AND RETURN A FONT OBJECT

```
# CREATE AND RETURN A FONT OBJECT #FONTS
# pygame.font.Font() creates font objects that we can use to render text.
# The first argument is None, meaning we use Pygame's default font.
# The second argument determines the font size.
#
# We create separate font objects because different parts of the game
# need different text sizes.
```

---

## CREATING RECTANGLES FOR THE CHOICES

```
# CREATING RECTANGLES FOR THE CHOICES .....
# pygame.Rect() creates rectangular objects.
# Each rectangle takes four measurements:
# X position, Y position, width and height.
#
# Making them to be on the same level = same y-axis value.
# All three buttons have the same Y position so that they appear horizontally.
#
# We store the rectangles inside a list because we need to access and
# manipulate all three buttons using loops.
```

---

## USING THE FONT OBJECT TO RENDER SURFACES

```
# USING THE FONT OBJECT WE CAN RENDER SURFACES FOR THE TEXT MESSAGES WE NEED
# pygame.font.Font() only creates the font object.
# To actually display text, we must render it into a surface.
#
# CENTRING THE TEXTS TO BE INSIDE THE RECTANGLES:
# We use get_rect(center=button.center) later to position the rendered
# option text at the exact centre of its corresponding button.
```

---

## INITIATE A TRUE LOOP

```
# INITIATE A TRUE LOOP
# running controls whether the game should continue executing.
# As long as running is True, the main game loop will keep repeating.
# When the player closes the window, we change running to False.
```

---

## FUNCTION DEFINITIONS

```
# FUNCTION DEFINITIONS

# FUNCTION TO ENSURE TEXT IS WRAPPED IN THE DESIRED BOX
# Long questions may exceed the available screen width.
# Instead of allowing the text to run off the screen, this function
# splits the question into multiple lines.
#
# Parameters:
# text       = The question or text we want to display.
# font       = The font object used to render the text.
# color      = The colour of the text.
# surface    = The surface on which the text will be drawn.
# x and y    = The position where the text should be centred.
# max_width  = The maximum permitted width of each line.
```

### draw_wrapped_text body comments

```
# split() separates the complete sentence into individual words.
# By default, it separates words wherever there is whitespace.

# We create an empty list that will store the completed lines.
# Each line will eventually be rendered separately.

# This variable temporarily stores the words being added to the current line.
# It starts empty because we have not added any words yet.

# We loop through every individual word obtained from text.split().

# We temporarily combine the current line with the next word.
# The extra space ensures that words do not get joined together.

# font.size() measures the width and height of the text.
# [0] retrieves the width.
#
# We check whether adding the next word would make the line
# exceed our maximum permitted width.

# If the line still fits, we accept the new word.
# current_line is updated to include the additional word.

# If the new word would make the line too wide,
# we save the previous completed line in our lines list.

# We then start a new line using the word that did not fit.

# After the loop finishes, we still need to save the final line.
# Otherwise, the last group of words would never be displayed.

# Now we loop through every completed line.
# Each line will be rendered and drawn separately.

# render() converts the text into a Pygame surface.
# True enables anti-aliasing, which makes the text appear smoother.
# color determines the colour of the rendered text.

# get_rect(center=(x, y)) creates a rectangle around the text
# and positions its centre at the coordinates we provide.

# blit() draws the rendered text surface onto our display surface.

# We increase the Y position by the font's line height.
# This moves the next line downwards instead of drawing it
# directly over the previous line.
```

---

## draw_question() function

```
# 1. RETRIEVE Q, RENDER QUE_TEXT, RENDER 3 BUTTON OPTIONS, DRAW THE BUTTONS
#
# This function is responsible for drawing the question screen.
# It retrieves the current question, displays the game title,
# displays the progress counter, draws the question and finally
# creates the three answer buttons.

# We retrieve the dictionary belonging to the current question.
# current_question determines which dictionary we access.
#
# For example, if current_question = 0, we retrieve questions[0].
# This gives us access to that question's text, options and answer.

# DRAW GAME TITLE
# render() converts NGOSOFY into a drawable text surface.
# True enables smooth text rendering.
# dark_brown determines the title's colour.

# get_rect(center=...) positions the title at the centre coordinates.
# blit() then draws the title onto our display surface.

# RENDERING SMALL SUBTITLE
# This creates the smaller descriptive text underneath the title.
# We use small_font because the subtitle should not be as large
# as the main game title.

# RENDERING QUESTION COUNTER
# This displays the player's current progress through the game.
#
# current_question + 1 is necessary because Python starts counting
# list indexes from zero, but we want the player to see question 1 first.
#
# len(questions) calculates the total number of questions in our list.

# DRAWING ACTUAL QUESTION
# We retrieve the question text from our current question dictionary.
#
# draw_wrapped_text() is called instead of directly using render()
# because some questions are longer than others.
#
# We pass:
# The question text, its font, its colour, the display surface,
# its centre coordinates and the maximum line width.

# DRAWING THE ANSWER BUTTONS AND THEIR TEXT
# enumerate() allows us to loop through the buttons while also
# keeping track of each button's index.
#
# index represents the position of the button in the list.
# button represents the actual pygame.Rect object.

# We check whether the current button's index matches
# the index stored inside selected_option.
#
# If they match, the button is the currently selected option
# and should be highlighted gold.

# If the indexes do not match, the button is not selected
# and therefore retains its normal brown colour.

# pygame.draw.rect() draws the actual rectangular button.
#
# DISPLAYSURF = The surface on which the button is drawn.
# button_colour = The colour we selected above.
# button = The rectangle containing its position and dimensions.
# border_radius = 20 gives the rectangle rounded corners.

# We retrieve the option belonging to the current question.
#
# question_data['options'] accesses the list of three possible answers.
# [index] retrieves the particular answer corresponding to this button.
#
# We render the answer using option_font and white text.

# We use get_rect(center=button.center) to position the option text
# exactly in the middle of its corresponding button.
#
# button.center automatically retrieves the centre coordinates
# of the current rectangular button.
```

---

## MAIN GAME LOOP

```
# MAIN GAME LOOP
#
# This is the main engine that keeps the game running.
# It continuously checks for player input, updates the screen
# and redraws the current question.
#
# Without this loop, the Pygame window would open and immediately close.
```

### Game loop body comments

```
# Every iteration starts by filling the entire display surface
# with our beige background colour.
#
# This clears the previous frame so that new drawings do not
# overlap with old ones.

# DRAWING THE RECTANGULAR SURFACES
# pygame.event.get() retrieves the events that have occurred
# since the previous iteration of the game loop.
#
# Events include keyboard presses, mouse clicks and window closing.

# If the player clicks the window's close button,
# Pygame generates a QUIT event.
#
# We change running to False so that the main loop stops.

# KEYBOARD INPUT
# KEYDOWN is triggered when the player presses a keyboard key.
# We use event.key to identify which particular key was pressed.

# ESTABLISHING ABILITY TO CYCLE THROUGH THE KEYS
#
# If the player presses RIGHT or DOWN, we move the selection
# forward by one position.
#
# selected_option + 1 increases the current button index.
#
# % len(buttons) ensures that the index never exceeds
# the number of available buttons.
#
# For example:
# (2 + 1) % 3 = 0
#
# This means that pressing RIGHT on the third button
# takes the player back to the first button.

# If the player presses LEFT or UP, we move the selection
# backwards by one position.
#
# The modulo operator also allows us to wrap around
# from the first button to the last button.

# ENTER KEY: ANSWER SUBMISSION
#
# When the player presses ENTER, we want to submit
# whichever answer is currently highlighted.
#
# Before doing that, we perform two checks:
#
# 1. selected_option != -1:
# This ensures that the player has actually selected
# one of the three available answers.
#
# 2. not answered:
# This checks whether the current question has already
# been submitted.
#
# The NOT operator reverses the Boolean value.
# Therefore, not answered is True when answered is False.
#
# Both conditions must be True before submission can happen.

# RETRIEVING THE PLAYER'S SELECTED ANSWER
#
# questions[current_question] retrieves the current
# question dictionary.
#
# ['options'] accesses its list of possible answers.
#
# [selected_option] retrieves the particular answer
# corresponding to the button selected by the player.
#
# We store this answer inside chosen_answer so that
# we can compare it with the correct answer.

# CHECKING WHETHER THE ANSWER IS CORRECT
#
# We compare the player's chosen_answer against
# the correct answer stored in the question dictionary.
#
# If both strings match, the condition evaluates to True.
# The score is then increased by one.
#
# If they do not match, the score remains unchanged.

# MARKING THE QUESTION AS ANSWERED
#
# Whether the answer was correct or incorrect,
# we now mark the question as answered.
#
# This prevents the player from pressing ENTER again
# and repeatedly submitting the same question.
#
# We will eventually use this variable to control
# the feedback screen and movement to the next question.

# ESTABLISHING PROPER MOUSE BUTTON RESPONSE
#
# MOUSEBUTTONDOWN is triggered when the player presses
# one of the mouse buttons.
#
# event.button identifies which mouse button was pressed.
# Button 1 represents the left mouse button.

# enumerate() allows us to inspect every button
# while keeping track of its index.
#
# event.pos retrieves the coordinates of the mouse
# at the exact moment the click occurred.
#
# collidepoint() checks whether those coordinates
# fall inside the current button's rectangular area.

# If the mouse click occurred inside a button,
# we store that button's index inside selected_option.
#
# draw_question() will then detect the matching index
# and highlight that button gold.

# DRAWING THE CURRENT QUESTION
#
# Once all events have been checked and processed,
# we call draw_question() to display the current game screen.
#
# This redraws the title, subtitle, progress counter,
# question and answer buttons.

# UPDATING THE DISPLAY
#
# pygame.display.flip() updates the entire display surface.
#
# All the drawings we performed during this iteration
# become visible to the player.
#
# Without this instruction, the changes made to the display
# would not be presented on the screen.
```

---

## EXITING THE GAME

```
# EXITING THE GAME
#
# Once running becomes False, the main game loop ends.
#
# pygame.quit() shuts down the initialized Pygame modules
# and releases the resources used by the game.
```
