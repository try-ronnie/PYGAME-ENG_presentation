import pygame


# QUESTIONS THAT RUN THE GAME
questions = [
    {
        'q_no': 0,
        'question': "Kate went to the pet store to buy a new ___",
        'options': ['beach', 'bitch', 'pitch'],
        'answer': 'bitch',
        'explanation': 'Bitch, in its non-slang use, means a female dog.'
    },

    {
        'q_no': 1,
        'question': 'Kiptoo went to buy a new _____ to wear because of the cold',
        'options': ['chaget', 'jacket', 'gasket'],
        'answer': 'jacket',
        'explanation': 'A jacket is an item of clothing worn to keep warm.'
    },

    {
        'q_no': 2,
        'question': 'Harry went over to send his warm ____ to the family upon hearing the disaster',
        'options': ['retards', 'regards', 'readers'],
        'answer': 'regards',
        'explanation': 'Regards are used to express good wishes or sympathy.'
    },

    {
        'q_no': 3,
        'question': 'If you have any questions, please do not hesitate to _____ me',
        'options': ['contract', 'contact', 'contrast'],
        'answer': 'contact',
        'explanation': 'Contact means to communicate or get in touch with someone.'
    },

    {
        'q_no': 4,
        'question': 'Jane really needed _____ on how to move forward',
        'options': ['advice', 'advise', 'add vice'],
        'answer': 'advice',
        'explanation': 'Advice is a noun referring to a recommendation. Advise is the verb.'
    },

    {
        'q_no': 5,
        'question': 'The manager sent a company-wide email to give everyone a _______ about the deadline',
        'options': ['gentle reminder', 'gental remainder', 'genital reminder'],
        'answer': 'gentle reminder',
        'explanation': 'A gentle reminder is a polite way of reminding someone about something.'
    },

    {
        'q_no': 6,
        'question': 'My father sent me to the garden to pick up the ____ used for digging',
        'options': ['hoe', 'hole', 'hone'],
        'answer': 'hoe',
        'explanation': 'A hoe is a gardening tool used for digging and cultivating soil.'
    },

    {
        'q_no': 7,
        'question': 'During the pandemic, we were always told to ______ our hands',
        'options': ['satanize', 'sanitize', 'santanize'],
        'answer': 'sanitize',
        'explanation': 'Sanitize means to clean something to reduce or eliminate germs.'
    },

    {
        'q_no': 8,
        'question': 'Our uncle brought back a Christmas bag full of ______',
        'options': ['treats', 'threats', 'krests'],
        'answer': 'treats',
        'explanation': 'Treats are enjoyable things such as sweets, snacks or small gifts.'
    },

    {
        'q_no': 9,
        'question': 'I woke up today feeling so _____',
        'options': ['gay', 'play', 'grade'],
        'answer': 'gay',
        'explanation': 'Gay can also mean feeling happy or cheerful.'
    },

    {
        'q_no': 10,
        'question': 'You know I can _____ you clearly, right?',
        'options': ['here', 'hear', 'where'],
        'answer': 'hear',
        'explanation': 'Hear means to perceive sound with your ears.'
    },

    {
        'q_no': 11,
        'question': 'She jerked ____ the stuck drawer until it opened',
        'options': ['off', 'at', 'upon'],
        'answer': 'at',
        'explanation': 'Jerk at means to make a sudden, sharp pulling movement.'
    },

    {
        'q_no': 12,
        'question': 'Please review the bed______ before taking it home',
        'options': ['sheet', 'shit', 'cheat'],
        'answer': 'sheet',
        'explanation': 'A sheet is a piece of bedding used to cover a mattress.'
    }
]


# ADDITIONAL VARIABLES
current_question = 0
score = 0
selected_option = -1
answered = False
game_finished = False


# SCREEN MEASUREMENTS
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900


# INITIALIZE THE LIBRARY
pygame.init()

# CREATE THE DISPLAY SURFACE
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('NGOSOFY')


# CREATE THE REQUIRED COLOUR VARIABLES
white = (255, 255, 255)
black = (0, 0, 0)
brown = (101, 67, 33)
dark_brown = (65, 42, 24)
beige = (245, 237, 220)
gold = (218, 165, 75)
green = (0, 128, 0)
red = (180, 40, 40)


# CREATE AND RETURN A FONT OBJECT #FONTS
title_font = pygame.font.Font(None, 96)
question_font = pygame.font.Font(None, 58)
option_font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 38)


# CREATING RECTANGLES FOR THE CHOICES
buttons = [
    pygame.Rect(80, 590, 440, 120),
    pygame.Rect(580, 590, 440, 120),
    pygame.Rect(1080, 590, 440, 120)
]


# FUNCTION DEFINITIONS

# FUNCTION TO ENSURE TEXT IS WRAPPED IN DESIRED BOX
def draw_wrapped_text(text, font, color, surface, x, y, max_width):

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "

        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + " "

    lines.append(current_line)

    for line in lines:
        text_surface = font.render(line, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, text_rect)
        y += font.get_linesize()


# DRAW THE QUESTION SCREEN
def draw_question():

    question_data = questions[current_question]

    # Game title
    title = title_font.render('NGOSOFY', True, dark_brown)
    DISPLAYSURF.blit(title, title.get_rect(center=(800, 80)))

    # Subtitle
    subtitle = small_font.render(
        'common spelling mistakes and context based errors',
        True, brown
    )
    DISPLAYSURF.blit(subtitle, subtitle.get_rect(center=(800, 145)))

    # Question counter
    progress = small_font.render(
        f'QUESTION : {current_question + 1} / {len(questions)}',
        True, brown
    )
    DISPLAYSURF.blit(progress, progress.get_rect(center=(800, 230)))

    # Actual question
    draw_wrapped_text(
        question_data['question'],
        question_font,
        dark_brown,
        DISPLAYSURF,
        800, 390, 1400
    )

    # Answer buttons and their text
    for index, button in enumerate(buttons):

        if index == selected_option:
            button_colour = gold
        else:
            button_colour = brown

        pygame.draw.rect(
            DISPLAYSURF,
            button_colour,
            button,
            border_radius=20
        )

        option_text = option_font.render(
            question_data['options'][index],
            True,
            white
        )

        DISPLAYSURF.blit(
            option_text,
            option_text.get_rect(center=button.center)
        )


# DRAW THE FEEDBACK SCREEN
def draw_feedback():

    question_data = questions[current_question]

    chosen_answer = question_data['options'][selected_option]
    correct_answer = question_data['answer']

    # Determine whether the submitted answer was correct
    if chosen_answer == correct_answer:
        feedback_message = "CORRECT!"
        feedback_colour = green
    else:
        feedback_message = "INCORRECT!"
        feedback_colour = red

    # Feedback message
    feedback_text = title_font.render(
        feedback_message,
        True,
        feedback_colour
    )

    DISPLAYSURF.blit(
        feedback_text,
        feedback_text.get_rect(center=(800, 300))
    )

    # Correct answer
    answer_text = question_font.render(
        f"Correct answer: {correct_answer}",
        True,
        dark_brown
    )

    DISPLAYSURF.blit(
        answer_text,
        answer_text.get_rect(center=(800, 420))
    )

    # Explanation
    draw_wrapped_text(
        question_data['explanation'],
        option_font,
        brown,
        DISPLAYSURF,
        800, 530, 1300
    )

    # Continue instruction
    continue_text = small_font.render(
        "PRESS ENTER TO CONTINUE",
        True,
        dark_brown
    )

    DISPLAYSURF.blit(
        continue_text,
        continue_text.get_rect(center=(800, 750))
    )


# DRAW THE FINAL RESULTS SCREEN
def draw_final_screen():

    # Final title
    title = title_font.render('GAME COMPLETED!', True, dark_brown)
    DISPLAYSURF.blit(title, title.get_rect(center=(800, 250)))

    # Final score
    final_score = question_font.render(
        f'YOUR SCORE: {score} / {len(questions)}',
        True,
        brown
    )

    DISPLAYSURF.blit(
        final_score,
        final_score.get_rect(center=(800, 400))
    )

    # Display a message based on the final score
    if score == len(questions):
        message = "PERFECT SCORE! WELL DONE!"
    elif score >= len(questions) / 2:
        message = "GOOD JOB! KEEP PRACTISING!"
    else:
        message = "KEEP LEARNING. YOU'LL GET BETTER!"

    result_message = option_font.render(message, True, dark_brown)

    DISPLAYSURF.blit(
        result_message,
        result_message.get_rect(center=(800, 520))
    )


# MAIN GAME LOOP
running = True

while running:

    DISPLAYSURF.fill(beige)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            # Keyboard navigation while answering
            if not answered and not game_finished:

                if event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(buttons)

                elif event.key == pygame.K_LEFT or event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(buttons)

                # Submit answer
                elif event.key == pygame.K_RETURN:

                    if selected_option != -1:

                        chosen_answer = questions[current_question]['options'][selected_option]

                        if chosen_answer == questions[current_question]['answer']:
                            score += 1

                        answered = True

            # Move to the next question after feedback
            elif event.key == pygame.K_RETURN and answered:

                if current_question < len(questions) - 1:

                    current_question += 1
                    selected_option = -1
                    answered = False

                else:
                    game_finished = True

        # Mouse selection
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1 and not answered and not game_finished:

                for index, button in enumerate(buttons):

                    if button.collidepoint(event.pos):
                        selected_option = index

    # Decide which screen to display
    if game_finished:
        draw_final_screen()

    elif answered:
        draw_feedback()

    else:
        draw_question()

    pygame.display.flip()


# CLOSE PYGame
pygame.quit()