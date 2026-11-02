
import pygame

# INITIALIZE
pygame.init()

# SCREEN
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NGOSOFY")

clock = pygame.time.Clock()


# COLOURS
beige = (245, 237, 220)
white = (255, 253, 248)
brown = (101, 67, 33)
dark_brown = (65, 42, 24)
gold = (218, 165, 75)
light_gold = (240, 220, 175)
green = (65, 135, 85)
red = (185, 75, 65)
grey = (130, 120, 105)


# FONTS
title_font = pygame.font.Font(None, 90)
subtitle_font = pygame.font.Font(None, 32)
question_font = pygame.font.Font(None, 55)
option_font = pygame.font.Font(None, 42)
small_font = pygame.font.Font(None, 30)
feedback_font = pygame.font.Font(None, 46)


# QUESTIONS
questions = [
    {
        'question': "Kate went to the pet store to buy a new ___",
        'options': ['beach', 'bitch', 'pitch'],
        'answer': 'bitch',
        'explanation': 'Bitch, in its non-slang use, means a female dog.'
    },

    {
        'question': 'Kiptoo went to buy a new _____ to wear because of the cold',
        'options': ['chaget', 'jacket', 'gasket'],
        'answer': 'jacket',
        'explanation': 'A jacket is an item of clothing worn to keep warm.'
    },

    {
        'question': 'Harry went over to send his warm ____ to the family upon hearing the disaster',
        'options': ['retards', 'regards', 'readers'],
        'answer': 'regards',
        'explanation': 'Regards are used to express good wishes or sympathy.'
    },

    {
        'question': 'If you have any questions, please do not hesitate to _____ me',
        'options': ['contract', 'contact', 'contrast'],
        'answer': 'contact',
        'explanation': 'Contact means to communicate or get in touch with someone.'
    },

    {
        'question': 'Jane really needed _____ on how to move forward',
        'options': ['advice', 'advise', 'add vice'],
        'answer': 'advice',
        'explanation': 'Advice is a noun referring to a recommendation. Advise is the verb.'
    },

    {
        'question': 'The manager sent a company-wide email to give everyone a _______ about the deadline',
        'options': ['gentle reminder', 'gental remainder', 'genital reminder'],
        'answer': 'gentle reminder',
        'explanation': 'A gentle reminder is a polite way of reminding someone about something.'
    },

    {
        'question': 'My father sent me to the garden to pick up the ____ used for digging',
        'options': ['hoe', 'hole', 'hone'],
        'answer': 'hoe',
        'explanation': 'A hoe is a gardening tool used for digging and cultivating soil.'
    },

    {
        'question': 'During the pandemic, we were always told to ______ our hands',
        'options': ['satanize', 'sanitize', 'santanize'],
        'answer': 'sanitize',
        'explanation': 'Sanitize means to clean something to reduce or eliminate germs.'
    },

    {
        'question': 'Our uncle brought back a Christmas bag full of ______',
        'options': ['treats', 'threats', 'krests'],
        'answer': 'treats',
        'explanation': 'Treats are enjoyable things such as sweets, snacks or small gifts.'
    },

    {
        'question': 'I woke up today feeling so _____',
        'options': ['gay', 'play', 'grade'],
        'answer': 'gay',
        'explanation': 'Gay can also mean feeling happy or cheerful.'
    },

    {
        'question': 'You know I can _____ you clearly, right?',
        'options': ['here', 'hear', 'where'],
        'answer': 'hear',
        'explanation': 'Hear means to perceive sound with your ears.'
    },

    {
        'question': 'She jerked ____ the stuck drawer until it opened',
        'options': ['off', 'at', 'upon'],
        'answer': 'at',
        'explanation': 'Jerk at means to make a sudden, sharp pulling movement.'
    },

    {
        'question': 'Please review the bed______ before taking it home',
        'options': ['sheet', 'shit', 'cheat'],
        'answer': 'sheet',
        'explanation': 'A sheet is a piece of bedding used to cover a mattress.'
    }
]


# GAME VARIABLES
current_question = 0
score = 0
selected_option = -1
answered = False
game_finished = False
running = True


# BUTTON POSITIONS
buttons = [
    pygame.Rect(120, 600, 420, 115),
    pygame.Rect(590, 600, 420, 115),
    pygame.Rect(1060, 600, 420, 115)
]


# TEXT WRAPPING FUNCTION
def draw_wrapped_text(text, font, colour, surface, x, y, max_width):

    words = text.split()
    lines = []
    current_line = ""

    for word in words:

        test_line = current_line + word + " "

        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)

            current_line = word + " "

    if current_line:
        lines.append(current_line)

    for line in lines:

        text_surface = font.render(line, True, colour)
        text_rect = text_surface.get_rect(center=(x, y))

        surface.blit(text_surface, text_rect)

        y += font.get_linesize()

    return y


# DRAW ROUNDED CARD
def draw_card(rect, colour, border_colour=None):

    pygame.draw.rect(
        DISPLAYSURF,
        colour,
        rect,
        border_radius=25
    )

    if border_colour:
        pygame.draw.rect(
            DISPLAYSURF,
            border_colour,
            rect,
            width=3,
            border_radius=25
        )


# GAME HEADER
def draw_header():

    title = title_font.render("NGOSOFY", True, dark_brown)

    DISPLAYSURF.blit(
        title,
        title.get_rect(center=(800, 75))
    )

    subtitle = subtitle_font.render(
        "COMMON SPELLING MISTAKES & CONTEXTUAL ERRORS",
        True,
        brown
    )

    DISPLAYSURF.blit(
        subtitle,
        subtitle.get_rect(center=(800, 130))
    )


# PROGRESS BAR
def draw_progress():

    progress_text = small_font.render(
        f"QUESTION {current_question + 1} / {len(questions)}",
        True,
        brown
    )

    DISPLAYSURF.blit(
        progress_text,
        (160, 190)
    )

    # Background of progress bar
    pygame.draw.rect(
        DISPLAYSURF,
        light_gold,
        (160, 230, 1280, 16),
        border_radius=10
    )

    # Filled portion
    progress_width = int(
        1280 * (current_question + 1) / len(questions)
    )

    pygame.draw.rect(
        DISPLAYSURF,
        gold,
        (160, 230, progress_width, 16),
        border_radius=10
    )


# DRAW QUESTION SCREEN
def draw_question():

    question_data = questions[current_question]

    draw_header()
    draw_progress()

    # Question card
    question_card = pygame.Rect(140, 290, 1320, 230)

    draw_card(
        question_card,
        white,
        light_gold
    )

    draw_wrapped_text(
        question_data['question'],
        question_font,
        dark_brown,
        DISPLAYSURF,
        800,
        375,
        1180
    )

    # Answer buttons
    for index, button in enumerate(buttons):

        if index == selected_option:
            button_colour = gold
            border_colour = dark_brown
        else:
            button_colour = white
            border_colour = light_gold

        draw_card(
            button,
            button_colour,
            border_colour
        )

        option_text = option_font.render(
            question_data['options'][index],
            True,
            dark_brown
        )

        DISPLAYSURF.blit(
            option_text,
            option_text.get_rect(center=button.center)
        )

    instruction = small_font.render(
        "USE ARROW KEYS OR MOUSE TO SELECT  |  PRESS ENTER TO SUBMIT",
        True,
        grey
    )

    DISPLAYSURF.blit(
        instruction,
        instruction.get_rect(center=(800, 800))
    )


# DRAW NOSO THE CARTOON CHARACTER
def draw_noso(x, y):

    # Body
    pygame.draw.ellipse(
        DISPLAYSURF,
        brown,
        (x - 65, y + 45, 130, 145)
    )

    # Head
    pygame.draw.circle(
        DISPLAYSURF,
        (235, 190, 145),
        (x, y),
        65
    )

    # Hair
    pygame.draw.arc(
        DISPLAYSURF,
        dark_brown,
        (x - 65, y - 65, 130, 100),
        0,
        3.14,
        13
    )

    # Eyes
    pygame.draw.circle(
        DISPLAYSURF,
        dark_brown,
        (x - 23, y - 5),
        6
    )

    pygame.draw.circle(
        DISPLAYSURF,
        dark_brown,
        (x + 23, y - 5),
        6
    )

    # Smile
    pygame.draw.arc(
        DISPLAYSURF,
        dark_brown,
        (x - 20, y + 5, 40, 30),
        3.14,
        6.28,
        4
    )

    # Little graduation cap
    pygame.draw.polygon(
        DISPLAYSURF,
        dark_brown,
        [
            (x - 70, y - 60),
            (x, y - 90),
            (x + 70, y - 60),
            (x, y - 35)
        ]
    )

    pygame.draw.line(
        DISPLAYSURF,
        gold,
        (x + 65, y - 60),
        (x + 75, y - 25),
        5
    )

    pygame.draw.circle(
        DISPLAYSURF,
        gold,
        (x + 75, y - 22),
        6
    )


# DRAW FEEDBACK SCREEN
def draw_feedback():

    question_data = questions[current_question]

    chosen_answer = question_data['options'][selected_option]
    correct_answer = question_data['answer']

    draw_header()

    # Feedback card
    feedback_card = pygame.Rect(120, 210, 1360, 570)

    draw_card(
        feedback_card,
        white,
        light_gold
    )

    # Determine whether answer was correct
    if chosen_answer == correct_answer:

        message = "EXCELLENT! YOU GOT IT RIGHT!"
        message_colour = green

    else:

        message = "NOT QUITE! LET'S LEARN!"
        message_colour = red

    feedback_text = feedback_font.render(
        message,
        True,
        message_colour
    )

    DISPLAYSURF.blit(
        feedback_text,
        feedback_text.get_rect(center=(800, 285))
    )

    # Correct answer
    answer_text = question_font.render(
        f"Correct answer: {correct_answer}",
        True,
        dark_brown
    )

    DISPLAYSURF.blit(
        answer_text,
        answer_text.get_rect(center=(700, 385))
    )

    # Character's speech bubble
    speech_bubble = pygame.Rect(180, 460, 970, 210)

    draw_card(
        speech_bubble,
        beige,
        light_gold
    )

    # Explanation
    explanation_title = small_font.render(
        "NOSO EXPLAINS:",
        True,
        brown
    )

    DISPLAYSURF.blit(
        explanation_title,
        (220, 490)
    )

    draw_wrapped_text(
        question_data['explanation'],
        option_font,
        dark_brown,
        DISPLAYSURF,
        665,
        565,
        850
    )

    # Draw Noso beside the speech bubble
    draw_noso(1300, 550)

    # Character label
    character_name = small_font.render(
        "NOSO",
        True,
        brown
    )

    DISPLAYSURF.blit(
        character_name,
        character_name.get_rect(center=(1300, 755))
    )

    # Continue instruction
    continue_text = small_font.render(
        "PRESS ENTER TO CONTINUE",
        True,
        dark_brown
    )

    DISPLAYSURF.blit(
        continue_text,
        continue_text.get_rect(center=(800, 835))
    )


# FINAL RESULTS SCREEN
def draw_final_screen():

    draw_header()

    result_card = pygame.Rect(250, 230, 1100, 480)

    draw_card(
        result_card,
        white,
        light_gold
    )

    title = title_font.render(
        "GAME COMPLETED!",
        True,
        dark_brown
    )

    DISPLAYSURF.blit(
        title,
        title.get_rect(center=(800, 320))
    )

    final_score = question_font.render(
        f"YOUR SCORE: {score} / {len(questions)}",
        True,
        brown
    )

    DISPLAYSURF.blit(
        final_score,
        final_score.get_rect(center=(800, 430))
    )

    if score == len(questions):
        message = "PERFECT SCORE! WELL DONE!"

    elif score >= len(questions) / 2:
        message = "GREAT WORK! KEEP LEARNING!"

    else:
        message = "KEEP PRACTISING. YOU'LL IMPROVE!"

    result_message = option_font.render(
        message,
        True,
        green if score >= len(questions) / 2 else red
    )

    DISPLAYSURF.blit(
        result_message,
        result_message.get_rect(center=(800, 530))
    )

    draw_noso(800, 640)


# MAIN GAME LOOP
while running:

    DISPLAYSURF.fill(beige)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            # Keyboard navigation
            if not answered and not game_finished:

                if event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:

                    selected_option = (
                        selected_option + 1
                    ) % len(buttons)

                elif event.key == pygame.K_LEFT or event.key == pygame.K_UP:

                    selected_option = (
                        selected_option - 1
                    ) % len(buttons)

                # Submit answer
                elif event.key == pygame.K_RETURN:

                    if selected_option != -1:

                        chosen_answer = questions[current_question]['options'][selected_option]

                        if chosen_answer == questions[current_question]['answer']:
                            score += 1

                        answered = True

            # Move to next question
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

    # Choose which screen to display
    if game_finished:

        draw_final_screen()

    elif answered:

        draw_feedback()

    else:

        draw_question()

    pygame.display.flip()

    clock.tick(60)


# CLOSE PYGAME
pygame.quit()