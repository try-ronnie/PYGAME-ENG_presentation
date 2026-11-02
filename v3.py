import pygame
import math

pygame.init()

# --------------------------------------------------
# SETUP
# --------------------------------------------------
WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NGOSOFY - The Language Game")
CLOCK = pygame.time.Clock()

# Colour palette
BG = (247, 242, 232)
CARD = (255, 253, 248)
CARD_SHADOW = (225, 216, 201)
INK = (62, 43, 31)  # deep brown
BROWN = (111, 77, 52)
MUTED = (145, 125, 105)
GOLD = (204, 158, 82)
GOLD_LIGHT = (239, 222, 188)
GREEN = (65, 133, 99)
GREEN_LIGHT = (226, 241, 230)
RED = (181, 91, 78)
RED_LIGHT = (248, 231, 226)
SKIN = (232, 183, 139)
SKIN_SHADOW = (203, 145, 104)
HAIR = (54, 37, 29)
WHITE = (255, 255, 255)

# Fonts
title_font = pygame.font.SysFont("georgia", 68, bold=True)
subtitle_font = pygame.font.SysFont("trebuchetms", 23)
question_font = pygame.font.SysFont("trebuchetms", 48, bold=True)
option_font = pygame.font.SysFont("trebuchetms", 37, bold=True)
body_font = pygame.font.SysFont("trebuchetms", 30)
feedback_font = pygame.font.SysFont("georgia", 38, bold=True)
small_font = pygame.font.SysFont("arial", 22)
tiny_font = pygame.font.SysFont("arial", 18, bold=True)

# --------------------------------------------------
# QUESTIONS
# --------------------------------------------------
questions = [
    {
        "question": "Kate went to the pet store to buy a new ___",
        "options": ["beach", "bitch", "pitch"],
        "answer": "bitch",
        "explanation": "Bitch, in its non-slang use, means a female dog."
    },
    {
        "question": "Kiptoo went to buy a new _____ to wear because of the cold",
        "options": ["chaget", "jacket", "gasket"],
        "answer": "jacket",
        "explanation": "A jacket is an item of clothing worn to keep warm."
    },
    {
        "question": "Harry went over to send his warm ____ to the family upon hearing the disaster",
        "options": ["retards", "regards", "readers"],
        "answer": "regards",
        "explanation": "Regards are used to express good wishes or sympathy."
    },
    {
        "question": "If you have any questions, please do not hesitate to _____ me",
        "options": ["contract", "contact", "contrast"],
        "answer": "contact",
        "explanation": "Contact means to communicate or get in touch with someone."
    },
    {
        "question": "Jane really needed _____ on how to move forward",
        "options": ["advice", "advise", "add vice"],
        "answer": "advice",
        "explanation": "Advice is a noun referring to a recommendation. Advise is the verb."
    },
    {
        "question": "The manager sent a company-wide email to give everyone a _______ about the deadline",
        "options": ["gentle reminder", "gental remainder", "genital reminder"],
        "answer": "gentle reminder",
        "explanation": "A gentle reminder is a polite way of reminding someone about something."
    },
    {
        "question": "My father sent me to the garden to pick up the ____ used for digging",
        "options": ["hoe", "hole", "hone"],
        "answer": "hoe",
        "explanation": "A hoe is a gardening tool used for digging and cultivating soil."
    },
    {
        "question": "During the pandemic, we were always told to ______ our hands",
        "options": ["satanize", "sanitize", "santanize"],
        "answer": "sanitize",
        "explanation": "Sanitize means to clean something to reduce or eliminate germs."
    },
    {
        "question": "Our uncle brought back a Christmas bag full of ______",
        "options": ["treats", "threats", "krests"],
        "answer": "treats",
        "explanation": "Treats are enjoyable things such as sweets, snacks or small gifts."
    },
    {
        "question": "I woke up today feeling so _____",
        "options": ["gay", "play", "grade"],
        "answer": "gay",
        "explanation": "Gay can also mean feeling happy or cheerful."
    },
    {
        "question": "You know I can _____ you clearly, right?",
        "options": ["here", "hear", "where"],
        "answer": "hear",
        "explanation": "Hear means to perceive sound with your ears."
    },
    {
        "question": "She jerked ____ the stuck drawer until it opened",
        "options": ["off", "at", "upon"],
        "answer": "at",
        "explanation": "Jerk at means to make a sudden, sharp pulling movement."
    },
    {
        "question": "Please review the bed______ before taking it home",
        "options": ["sheet", "shit", "cheat"],
        "answer": "sheet",
        "explanation": "A sheet is a piece of bedding used to cover a mattress."
    }
]

# --------------------------------------------------
# GAME STATE
# --------------------------------------------------
current_question = 0
score = 0
selected_option = -1
answered = False
game_finished = False
running = True
answer_was_correct = False

buttons = [
    pygame.Rect(145, 610, 410, 112),
    pygame.Rect(595, 610, 410, 112),
    pygame.Rect(1045, 610, 410, 112)
]

# --------------------------------------------------
# DRAWING HELPERS
# --------------------------------------------------
def draw_text(text, font, colour, center):
    image = font.render(text, True, colour)
    SCREEN.blit(image, image.get_rect(center=center))


def draw_card(rect, fill=CARD, border=None, radius=24, shadow=True):
    if shadow:
        shadow_rect = rect.move(0, 8)
        pygame.draw.rect(SCREEN, CARD_SHADOW, shadow_rect, border_radius=radius)
    pygame.draw.rect(SCREEN, fill, rect, border_radius=radius)
    if border:
        pygame.draw.rect(SCREEN, border, rect, width=2, border_radius=radius)


def wrapped_lines(text, font, max_width):
    words = text.split()
    lines = []
    line = ""

    for word in words:
        test = f"{line} {word}".strip()
        if font.size(test)[0] <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = word

    if line:
        lines.append(line)

    return lines


def draw_wrapped_center(text, font, colour, center_x, start_y, max_width, line_gap=8):
    lines = wrapped_lines(text, font, max_width)
    line_height = font.get_linesize() + line_gap
    total_height = len(lines) * line_height - line_gap
    y = start_y - total_height // 2

    for line in lines:
        draw_text(line, font, colour, (center_x, y + font.get_linesize() // 2))
        y += line_height


def draw_wrapped_left(text, font, colour, x, y, max_width, line_gap=7):
    lines = wrapped_lines(text, font, max_width)
    for line in lines:
        image = font.render(line, True, colour)
        SCREEN.blit(image, (x, y))
        y += font.get_linesize() + line_gap


def draw_background():
    SCREEN.fill(BG)
    # Soft decorative corner shapes
    pygame.draw.circle(SCREEN, (240, 231, 213), (0, 0), 230)
    pygame.draw.circle(SCREEN, (241, 233, 218), (WIDTH, HEIGHT), 250)
    pygame.draw.circle(SCREEN, (250, 247, 240), (WIDTH, 0), 115)


def draw_header():
    draw_text("NGOSOFY", title_font, INK, (WIDTH // 2, 75))
    draw_text(
        "THE LANGUAGE GAME  •  LEARN THROUGH CONTEXT",
        subtitle_font, MUTED, (WIDTH // 2, 132)
    )
    pygame.draw.line(SCREEN, GOLD_LIGHT, (500, 166), (1100, 166), 3)


def draw_progress():
    label = f"QUESTION {current_question + 1:02d}  /  {len(questions):02d}"
    draw_text(label, tiny_font, BROWN, (205, 205))

    bar = pygame.Rect(205, 228, 1190, 13)
    pygame.draw.rect(SCREEN, GOLD_LIGHT, bar, border_radius=8)

    fill_width = int(bar.width * (current_question + 1) / len(questions))
    if fill_width > 0:
        pygame.draw.rect(
            SCREEN, GOLD,
            (bar.x, bar.y, fill_width, bar.height),
            border_radius=8
        )

    draw_text(f"SCORE  {score}", small_font, BROWN, (1320, 205))


# --------------------------------------------------
# NOSO CHARACTER
# --------------------------------------------------
def draw_noso(x, y, mood="idle", time_value=0):
    # Gentle floating motion
    bob = int(math.sin(time_value * 2.4) * 5)
    y += bob

    happy = mood == "happy"
    sad = mood == "sad"

    body_colour = BROWN
    arm_width = 13

    # Body
    pygame.draw.ellipse(SCREEN, body_colour, (x - 58, y + 48, 116, 132))
    pygame.draw.ellipse(SCREEN, INK, (x - 58, y + 48, 116, 132), 3)

    # Arms and hands
    if happy:
        left_hand = (x - 105, y + 35)
        right_hand = (x + 105, y + 35)
        left_elbow = (x - 72, y + 83)
        right_elbow = (x + 72, y + 83)
    elif sad:
        left_hand = (x - 92, y + 151)
        right_hand = (x + 92, y + 151)
        left_elbow = (x - 75, y + 115)
        right_elbow = (x + 75, y + 115)
    else:
        left_hand = (x - 93, y + 108)
        right_hand = (x + 93, y + 108)
        left_elbow = (x - 70, y + 91)
        right_elbow = (x + 70, y + 91)

    pygame.draw.line(SCREEN, body_colour, (x - 45, y + 85), left_elbow, arm_width)
    pygame.draw.line(SCREEN, body_colour, left_elbow, left_hand, arm_width)
    pygame.draw.line(SCREEN, body_colour, (x + 45, y + 85), right_elbow, arm_width)
    pygame.draw.line(SCREEN, body_colour, right_elbow, right_hand, arm_width)
    pygame.draw.circle(SCREEN, SKIN, left_hand, 11)
    pygame.draw.circle(SCREEN, SKIN, right_hand, 11)

    # Head and ears
    pygame.draw.circle(SCREEN, SKIN_SHADOW, (x - 59, y + 4), 15)
    pygame.draw.circle(SCREEN, SKIN_SHADOW, (x + 59, y + 4), 15)
    pygame.draw.circle(SCREEN, SKIN, (x, y), 67)
    pygame.draw.circle(SCREEN, INK, (x, y), 67, 3)

    # Hair
    pygame.draw.arc(SCREEN, HAIR, (x - 66, y - 67, 132, 88), 3.14, 6.28, 15)
    pygame.draw.circle(SCREEN, HAIR, (x - 42, y - 49), 15)
    pygame.draw.circle(SCREEN, HAIR, (x - 15, y - 62), 16)
    pygame.draw.circle(SCREEN, HAIR, (x + 15, y - 61), 15)
    pygame.draw.circle(SCREEN, HAIR, (x + 42, y - 48), 14)

    # Cheeks
    if happy:
        pygame.draw.circle(SCREEN, (224, 137, 124), (x - 43, y + 16), 9)
        pygame.draw.circle(SCREEN, (224, 137, 124), (x + 43, y + 16), 9)

    # Eyes and eyebrows
    if happy:
        pygame.draw.arc(SCREEN, INK, (x - 39, y - 13, 25, 20), 0, math.pi, 4)
        pygame.draw.arc(SCREEN, INK, (x + 14, y - 13, 25, 20), 0, math.pi, 4)
        pygame.draw.arc(SCREEN, INK, (x - 25, y + 12, 50, 37), math.pi, 2 * math.pi, 5)
    elif sad:
        pygame.draw.line(SCREEN, INK, (x - 39, y - 18), (x - 16, y - 11), 4)
        pygame.draw.line(SCREEN, INK, (x + 16, y - 11), (x + 39, y - 18), 4)
        pygame.draw.circle(SCREEN, INK, (x - 26, y - 1), 5)
        pygame.draw.circle(SCREEN, INK, (x + 26, y - 1), 5)
        pygame.draw.arc(SCREEN, INK, (x - 25, y + 32, 50, 30), 0, math.pi, 5)
        # Small tear drops
        pygame.draw.ellipse(SCREEN, (112, 171, 202), (x - 39, y + 4, 8, 15))
    else:
        pygame.draw.circle(SCREEN, INK, (x - 26, y - 5), 5)
        pygame.draw.circle(SCREEN, INK, (x + 26, y - 5), 5)
        pygame.draw.arc(SCREEN, INK, (x - 20, y + 16, 40, 25), math.pi, 2 * math.pi, 4)

    # Graduation cap
    pygame.draw.polygon(
        SCREEN, INK,
        [(x - 76, y - 56), (x, y - 91), (x + 76, y - 56), (x, y - 27)]
    )
    pygame.draw.polygon(
        SCREEN, BROWN,
        [(x - 42, y - 53), (x, y - 73), (x + 42, y - 53), (x, y - 36)]
    )
    pygame.draw.line(SCREEN, GOLD, (x + 70, y - 56), (x + 82, y - 20), 4)
    pygame.draw.circle(SCREEN, GOLD, (x + 82, y - 18), 6)


def draw_character_tag(text, colour, center):
    tag = pygame.Rect(0, 0, 180, 38)
    tag.center = center
    pygame.draw.rect(SCREEN, colour, tag, border_radius=18)
    draw_text(text, tiny_font, WHITE, tag.center)


# --------------------------------------------------
# QUESTION SCREEN
# --------------------------------------------------
def draw_question(time_value):
    draw_header()
    draw_progress()

    question_card = pygame.Rect(155, 285, 1290, 245)
    draw_card(question_card, CARD, (235, 225, 207))

    draw_text("CHOOSE THE WORD THAT FITS BEST", tiny_font, GOLD, (800, 330))
    draw_wrapped_center(
        questions[current_question]["question"],
        question_font, INK, 800, 420, 1160
    )

    for index, button in enumerate(buttons):
        hovered = button.collidepoint(pygame.mouse.get_pos())
        selected = index == selected_option

        if selected:
            fill, border = GOLD_LIGHT, GOLD
        elif hovered:
            fill, border = (250, 245, 235), GOLD_LIGHT
        else:
            fill, border = CARD, (232, 222, 205)

        draw_card(button, fill, border, radius=20, shadow=True)

        number_circle = (button.x + 43, button.centery)
        pygame.draw.circle(SCREEN, GOLD if selected else GOLD_LIGHT, number_circle, 19)
        draw_text(str(index + 1), tiny_font, WHITE if selected else BROWN, number_circle)

        option = questions[current_question]["options"][index]
        draw_text(option, option_font, INK, (button.centerx + 18, button.centery))

    draw_text(
        "ARROW KEYS / MOUSE TO SELECT     •     ENTER TO SUBMIT",
        small_font, MUTED, (800, 800)
    )
    draw_text("NGOSOFY", tiny_font, (184, 169, 149), (800, 850))


# --------------------------------------------------
# FEEDBACK SCREEN
# --------------------------------------------------
def draw_feedback(time_value):
    data = questions[current_question]
    chosen = data["options"][selected_option]
    correct = chosen == data["answer"]

    draw_header()

    mood = "happy" if correct else "sad"
    accent = GREEN if correct else RED
    tint = GREEN_LIGHT if correct else RED_LIGHT

    panel = pygame.Rect(115, 205, 1370, 585)
    draw_card(panel, CARD, (235, 225, 207))

    message = "BRILLIANT! THAT'S CORRECT!" if correct else "NOT QUITE — KEEP LEARNING!"
    draw_text(message, feedback_font, accent, (800, 275))

    # Result pill
    result_text = f"YOUR ANSWER: {chosen.upper()}"
    draw_text(result_text, small_font, MUTED, (800, 330))

    answer_box = pygame.Rect(230, 370, 790, 88)
    draw_card(answer_box, tint, None, radius=18, shadow=False)
    draw_text(f"CORRECT ANSWER: {data['answer']}", body_font, accent, answer_box.center)

    # Speech bubble
    bubble = pygame.Rect(205, 495, 850, 205)
    draw_card(bubble, (249, 245, 236), (235, 225, 207), radius=22, shadow=False)
    pygame.draw.polygon(
        SCREEN, (249, 245, 236),
        [(1025, 570), (1070, 590), (1025, 610)]
    )
    pygame.draw.line(SCREEN, (235, 225, 207), (1025, 570), (1070, 590), 2)
    pygame.draw.line(SCREEN, (235, 225, 207), (1070, 590), (1025, 610), 2)

    draw_text("NOSO EXPLAINS", tiny_font, GOLD, (360, 535))
    draw_wrapped_left(data["explanation"], body_font, INK, 265, 575, 730, 8)

    draw_noso(1260, 565, mood, time_value)
    draw_character_tag("HAPPY NOSO!" if correct else "SAD NOSO", accent, (1260, 760))

    draw_text("PRESS ENTER TO CONTINUE", small_font, BROWN, (800, 835))


# --------------------------------------------------
# FINAL SCREEN
# --------------------------------------------------
def draw_final_screen(time_value):
    draw_header()

    panel = pygame.Rect(250, 220, 1100, 540)
    draw_card(panel, CARD, (235, 225, 207))

    draw_text("GAME COMPLETED!", title_font, INK, (800, 310))
    draw_text("YOUR FINAL SCORE", small_font, MUTED, (800, 395))
    draw_text(f"{score} / {len(questions)}", title_font, GOLD, (800, 475))

    if score == len(questions):
        message = "PERFECT SCORE! YOU'RE A WORD WIZARD!"
        mood = "happy"
        accent = GREEN
    elif score >= len(questions) / 2:
        message = "GREAT WORK! KEEP BUILDING YOUR SKILLS!"
        mood = "happy"
        accent = GREEN
    else:
        message = "KEEP PRACTISING. EVERY WORD IS PROGRESS!"
        mood = "sad"
        accent = RED

    draw_text(message, body_font, accent, (800, 555))
    draw_noso(800, 650, mood, time_value)
    draw_text("CLOSE THE WINDOW TO EXIT", small_font, MUTED, (800, 825))


# --------------------------------------------------
# MAIN GAME LOOP
# --------------------------------------------------
while running:
    time_value = pygame.time.get_ticks() / 1000
    draw_background()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if not answered and not game_finished:
                if event.key in (pygame.K_RIGHT, pygame.K_DOWN):
                    selected_option = (selected_option + 1) % len(buttons)

                elif event.key in (pygame.K_LEFT, pygame.K_UP):
                    selected_option = (selected_option - 1) % len(buttons)

                elif event.key == pygame.K_RETURN and selected_option != -1:
                    chosen = questions[current_question]["options"][selected_option]
                    answer_was_correct = chosen == questions[current_question]["answer"]

                    if answer_was_correct:
                        score += 1

                    answered = True

            elif event.key == pygame.K_RETURN and answered:
                if current_question < len(questions) - 1:
                    current_question += 1
                    selected_option = -1
                    answered = False
                else:
                    game_finished = True

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not answered and not game_finished:
                for index, button in enumerate(buttons):
                    if button.collidepoint(event.pos):
                        selected_option = index

    if game_finished:
        draw_final_screen(time_value)
    elif answered:
        draw_feedback(time_value)
    else:
        draw_question(time_value)

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()
