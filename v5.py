import math
import random
import pygame



#NOTE ALL FUNCTIONS I DEVELOPED FROM V2 ARE CARRIED AND INITIATED IN THE LOOP WITH NO NECESSARY IMPROVEMENTS MADE
# THIS WILL BE THE FINAL VISUAL QUE
pygame.init()

# SCREEN
W, H = 1600, 900
screen = pygame.display.set_mode((W, H), pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("NGOSOFY")
clock = pygame.time.Clock()

# COLOUR PALETTE (warm cream / chocolate / gold, with soft green + red feedback)
CREAM_TOP = (251, 245, 232)
CREAM_BOT = (238, 224, 197)
CARD = (255, 252, 246)
BUBBLE = (250, 242, 225)
INK = (58, 38, 22)
BROWN = (112, 78, 46)
MUTED = (143, 119, 89)
GOLD = (214, 160, 66)
GOLD_DARK = (176, 125, 38)
GOLD_SOFT = (244, 225, 184)
GREEN = (52, 132, 85)
GREEN_SOFT = (214, 238, 220)
RED = (186, 74, 62)
RED_SOFT = (247, 217, 210)
SHADOW = (214, 198, 168)
SKIN = (236, 190, 148)
BLUSH = (244, 165, 145)
BLUE = (110, 165, 220)

# FONTS (first installed font in each list is used)
SERIF = "georgia,cambria,palatino,timesnewroman"
SANS = "trebuchetms,segoeui,calibri,verdana,arial"

f_title = pygame.font.SysFont(SERIF, 88, bold=True)
f_banner = pygame.font.SysFont(SERIF, 54, bold=True)
f_big = pygame.font.SysFont(SERIF, 130, bold=True)
f_q = pygame.font.SysFont(SERIF, 52)
f_opt = pygame.font.SysFont(SANS, 38, bold=True)
f_body = pygame.font.SysFont(SANS, 36)
f_pill = pygame.font.SysFont(SANS, 32, bold=True)
f_badge = pygame.font.SysFont(SANS, 32, bold=True)
f_small = pygame.font.SysFont(SANS, 25, bold=True)

# QUESTIONS
questions = [
    {'question': "Kate went to the pet store to buy a new ___",
    'options': ['beach', 'bitch', 'pitch'], 'answer': 'bitch',
    'explanation': 'Bitch, in its non-slang use, means a female dog.You almost thought of it huh'},

    {'question': 'Kiptoo went to buy a new _____ to wear because of the cold',
    'options': ['chaget', 'jacket', 'gasket'], 'answer': 'jacket',
    'explanation': 'A jacket is an item of clothing worn to keep warm.'},

    {'question': 'Harry went over to send his warm ____ to the family upon hearing the disaster',
    'options': ['retards', 'regards', 'readers'], 'answer': 'regards',
    'explanation': 'Regards are used to express good wishes or sympathy. Retards mean slow minded people'},

    {'question': 'If you have any questions, please do not hesitate to _____ me',
    'options': ['contract', 'contact', 'contrast'], 'answer': 'contact',
    'explanation': 'Contact means to communicate or get in touch with someone.'},

    {'question': 'Jane really needed _____ on how to move forward',
    'options': ['advice', 'advise', 'add vice'], 'answer': 'advice',
    'explanation': 'Advice is a noun referring to a recommendation. Advise is the verb.'},

    {'question': 'The manager sent a company-wide email to give everyone a _______ about the deadline',
    'options': ['gentle reminder', 'gental remainder', 'genital reminder'], 'answer': 'gentle reminder',
    'explanation': 'A gentle reminder is a polite way of reminding someone about something. Genital reminder is for people with stis '},

    {'question': 'My father sent me to the garden to pick up the ____ used for digging',
    'options': ['hoe', 'hole', 'hone'], 'answer': 'hoe',
    'explanation': 'A hoe is a gardening tool used for digging and cultivating soil.'},

    {'question': 'During the pandemic, we were always told to ______ our hands',
    'options': ['satanize', 'sanitize', 'santanize'], 'answer': 'sanitize',
    'explanation': 'Sanitize means to clean something to reduce or eliminate germs.'},

    {'question': 'Our uncle brought back a Christmas bag full of ______',
    'options': ['treats', 'threats', 'krests'], 'answer': 'treats',
    'explanation': 'Treats are enjoyable things such as sweets, snacks or small gifts. Well depending on your uncle'},

    {'question': 'I woke up today feeling so _____',
    'options': ['gay', 'play', 'grade'], 'answer': 'gay',
    'explanation': 'Gay can also mean feeling happy or cheerful.Besides its slang usage which means Homo-sexual'},

    {'question': 'You know I can _____ you clearly, right?',
    'options': ['here', 'hear', 'where'], 'answer': 'hear',
    'explanation': 'Hear means to perceive sound with your ears.'},

    {'question': 'She jerked ____ the stuck drawer until it opened',
    'options': ['off', 'at', 'upon'], 'answer': 'at',
    'explanation': 'Jerk at means to make a sudden, sharp pulling movement. I will not explain the first one ... use common sense'},

    {'question': 'Please review the bed______ before taking it home',
    'options': ['sheet', 'shit', 'cheat'], 'answer': 'sheet',
    'explanation': 'A sheet is a piece of bedding used to cover a mattress.'},

    {'question': "In french we say ______ before eating",
    'options': ['bone apple tea', 'boner apple tea', 'bon appetit'],
    'answer': 'bon appetit',
    'explanation': 'due to tik-tok brainrot , many forget the correct spelling which is bon appetit'
    },

    {'question': 'This is a ______ announcement from the private sector',
    'options': ['pubic', 'public', 'garlic'],
    'answer': 'public',
    'explanation': 'Public is correct meaning general info meant for each and every person.'
    },

    {'question': 'we need a totally ______ third party to judge the company contest',
    'options': ['uninterested', 'disinterested', 'ininterested'],
    'answer': 'disinterested',
    'explanation': 'disinterested - meaning a person who doesnt give two shits about the event... excuse my language ... some one completely bored for the occasion'
    },

    {'question': "we need to nip this problem ______",
    'options': ['in the bud', 'in the butt', 'in a nut'],
    'answer': 'in the bud',
    'explanation': 'in the bud - we use this to mean halting a problem early , if you chose any other one you need Jesus!!!!'
    },

    {'question': 'He was arrested for committing ____ and battery',
    'options': ['a salt', 'assert', 'assault'],
    'answer': 'assault',
    'explanation': 'assault to mean intentional hurting or causing another person to fear imminent physical harm'
    },

    {'question': 'The marsh is home to a unique , microscopic ______',
    'options': ['orgasm', 'organs', 'organism'],
    'answer': 'organism',
    'explanation': 'An organism is any living individual animal , plant , or single-celled life. Mostly confused with orgasm (meaning is obvious) due to the forgetten letter   i'
    },

    {'question': 'In 2027 all kenyans must stand strong for the ______ to be held , to remove the current president',
    'options': ['elections', 'erections', 'ejections'],
    'answer': 'elections',
    'explanation': 'elections - a practise held after sometime for the citizens to vote and choose their leaders'
    },

    {'question': 'He rode into the village sitting high upon his _____',
    'options': ['ass', 'ahh', 'ash'],
    'answer': 'ass',
    'explanation': 'Historically, an ass is a donkey or a stubborn animal.'
    },
    {'question' : 'During an emergence , make sure to _____ all of us',  
    'options' : ['ejaculate' , 'evacuate' , 'evaporate'],
    'answer' : 'evacuate' , 
    'explanation' : 'evacuate = to mean helping people to escape an endangered area'
    }
]
GOOD_MSGS = ["Excellent! You got it right!", "Spot on! Well done!", "Correct! Nicely spelled!"]
BAD_MSGS = ["Not quite, let's learn!", "Oops! Not this time.", "Good try! Here's the trick."]

# GAME STATE
state = "question"          # "question" | "feedback" | "final"
current = 0
score = 0
selected = -1
was_correct = False
feedback_msg = ""
feedback_start = 0
type_start = 0
final_start = 0
fade_start = 0
warn_until = 0
progress_anim = 0.0
confetti = []
running = True

BUTTONS = [pygame.Rect(120 + i * 470, 585, 420, 130) for i in range(3)]
KEY_CHOICES = {pygame.K_1: 0, pygame.K_a: 0, pygame.K_2: 1, pygame.K_b: 1, pygame.K_3: 2, pygame.K_c: 2}
TYPE_SPEED = 55  # characters per second for Noso's explanation


# HELPERS
def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def ease_out(p):
    return 1 - (1 - p) ** 3

# returning the colour schematic out
# function definition to remain the same in version2
def make_background():
    # Vertical gradient + a few faint gold circles, drawn once and reused every frame
    bg = pygame.Surface((W, H))
    for y in range(H):
        pygame.draw.line(bg, lerp(CREAM_TOP, CREAM_BOT, y / H), (0, y), (W, y))
    glow = pygame.Surface((W, H), pygame.SRCALPHA)
    for cx, cy, r in ((90, 120, 240), (1520, 800, 320), (1500, 80, 160)):
        pygame.draw.circle(glow, (214, 160, 66, 26), (cx, cy), r)
    bg.blit(glow, (0, 0))
    return bg


background = make_background()
fade_surface = pygame.Surface((W, H))
fade_surface.fill(CREAM_BOT)


def draw_card(rect, fill=CARD, border=GOLD_SOFT, radius=26, shadow=True):
    rect = pygame.Rect(rect)
    if shadow:
        pygame.draw.rect(screen, SHADOW, rect.move(0, 8), border_radius=radius)
    pygame.draw.rect(screen, fill, rect, border_radius=radius)
    if border:
        pygame.draw.rect(screen, border, rect, 3, border_radius=radius)


def wrap(text, font, max_w):
    lines, cur = [], ""
    for word in text.split():
        test = f"{cur} {word}".strip()
        if font.size(test)[0] <= max_w or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def block_height(text, font, max_w):
    return len(wrap(text, font, max_w)) * (font.get_linesize() + 4)


def draw_block(text, font, colour, x, y, max_w, center=True, chars=None):
    # Wraps text and draws it from y downward. 'chars' reveals only the first N characters (typewriter)
    remaining = len(text) if chars is None else chars
    for line in wrap(text, font, max_w):
        if remaining <= 0:
            break
        part = line[:remaining]
        remaining -= len(line) + 1
        surf = font.render(part, True, colour)
        rect = surf.get_rect(midtop=(x, y)) if center else surf.get_rect(topleft=(x, y))
        screen.blit(surf, rect)
        y += font.get_linesize() + 4
    return y


def draw_pill(text, x, y, fill, colour):
    surf = f_pill.render(text, True, colour)
    rect = pygame.Rect(x, y, surf.get_width() + 56, 56)
    pygame.draw.rect(screen, fill, rect, border_radius=28)
    screen.blit(surf, surf.get_rect(center=rect.center))
    return rect


def draw_star(cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + math.cos(ang) * rad, cy + math.sin(ang) * rad))
    pygame.draw.polygon(screen, fill, pts)


# CONFETTI
def spawn_confetti(n=90, cx=1290, cy=330):
    palette = [GOLD, GREEN, RED, BLUE, (240, 190, 90)]
    for _ in range(n):
        confetti.append({
            "x": cx, "y": cy,
            "vx": random.uniform(-400, 400), "vy": random.uniform(-720, -200),
            "c": random.choice(palette), "s": random.randint(8, 15),
            "life": random.uniform(1.5, 2.5),
        })


def update_confetti(dt):
    for p in confetti[:]:
        p["vy"] += 900 * dt
        p["x"] += p["vx"] * dt
        p["y"] += p["vy"] * dt
        p["life"] -= dt
        if p["life"] <= 0 or p["y"] > H:
            confetti.remove(p)


def draw_confetti():
    for p in confetti:
        pygame.draw.rect(screen, p["c"], (p["x"], p["y"], p["s"], p["s"] * 0.6))


# NOSO THE TEACHER
def draw_noso(x, y, mood, t):
    # mood: "idle", "happy" or "sad"; t = ms since the mood started (drives all animation)
    s = t / 1000
    if mood == "happy":
        amp = 6 + 22 * max(0, 1 - s / 2.5)      # big bounces that settle into a happy sway
        dy = -abs(math.sin(s * 5.5)) * amp
    elif mood == "sad":
        dy = 8 + math.sin(s * 1.6) * 3          # slumped and slowly swaying
    else:
        dy = math.sin(s * 2) * 5                # gentle idle bob

    lift = -dy
    sw = max(70, int(150 - lift * 1.5 - (10 if mood == "sad" else 0)))
    pygame.draw.ellipse(screen, SHADOW, (x - sw // 2, y + 198, sw, 26))   # ground shadow

    y += dy
    blink = pygame.time.get_ticks() % 3400 < 140

    # body + bow tie
    pygame.draw.ellipse(screen, BROWN, (x - 70, y + 50, 140, 150))
    pygame.draw.polygon(screen, GOLD, [(x, y + 78), (x - 26, y + 62), (x - 26, y + 94)])
    pygame.draw.polygon(screen, GOLD, [(x, y + 78), (x + 26, y + 62), (x + 26, y + 94)])
    pygame.draw.circle(screen, GOLD_DARK, (x, y + 78), 7)

    # arms
    if mood == "happy":
        wave = math.sin(s * 9)
        hands = [(x - 108, y + 28 + wave * 16), (x + 108, y + 28 - wave * 16)]
    elif mood == "sad":
        sag = math.sin(s * 1.6) * 3
        hands = [(x - 74, y + 172 + sag), (x + 74, y + 172 + sag)]
    else:
        hands = [(x - 90, y + 148), (x + 90, y + 148)]
    for (hx, hy), sx in zip(hands, (x - 52, x + 52)):
        pygame.draw.line(screen, BROWN, (sx, y + 100), (hx, hy), 15)
        pygame.draw.circle(screen, SKIN, (int(hx), int(hy)), 12)

    # head + hair
    pygame.draw.circle(screen, SKIN, (x, y), 66)
    pygame.draw.arc(screen, INK, (x - 66, y - 66, 132, 110), 0, math.pi, 14)

    # face
    if mood == "happy":
        pygame.draw.circle(screen, BLUSH, (x - 42, y + 20), 11)
        pygame.draw.circle(screen, BLUSH, (x + 42, y + 20), 11)
        pygame.draw.arc(screen, INK, (x - 38, y - 14, 28, 22), 0, math.pi, 5)   # ^ ^ eyes
        pygame.draw.arc(screen, INK, (x + 10, y - 14, 28, 22), 0, math.pi, 5)
        pygame.draw.ellipse(screen, INK, (x - 22, y + 14, 44, 28))              # open smile
        pygame.draw.ellipse(screen, SKIN, (x - 22, y + 14, 44, 13))
        pygame.draw.ellipse(screen, BLUSH, (x - 11, y + 31, 22, 9))
    elif mood == "sad":
        pygame.draw.line(screen, INK, (x - 40, y - 22), (x - 14, y - 32), 5)     # worried brows
        pygame.draw.line(screen, INK, (x + 40, y - 22), (x + 14, y - 32), 5)
        if blink:
            pygame.draw.line(screen, INK, (x - 32, y - 2), (x - 14, y - 2), 4)
            pygame.draw.line(screen, INK, (x + 14, y - 2), (x + 32, y - 2), 4)
        else:
            for ex in (x - 23, x + 23):
                pygame.draw.circle(screen, INK, (ex, y - 2), 8)
                pygame.draw.circle(screen, CARD, (ex - 2, y - 5), 3)
        pygame.draw.arc(screen, INK, (x - 22, y + 28, 44, 26), 0, math.pi, 5)    # frown
        ty = y + 8 + ((s % 1.4) / 1.4) * 60                                      # falling tear
        pygame.draw.circle(screen, BLUE, (x - 26, int(ty)), 6)
    else:
        if blink:
            pygame.draw.line(screen, INK, (x - 32, y - 4), (x - 14, y - 4), 4)
            pygame.draw.line(screen, INK, (x + 14, y - 4), (x + 32, y - 4), 4)
        else:
            for ex in (x - 23, x + 23):
                pygame.draw.circle(screen, INK, (ex, y - 4), 7)
                pygame.draw.circle(screen, CARD, (ex - 2, y - 7), 2)
        pygame.draw.arc(screen, INK, (x - 20, y + 8, 40, 26), math.pi, 2 * math.pi, 5)

    # graduation cap + swinging tassel
    cap_y = y + (6 if mood == "sad" else 0)
    pygame.draw.polygon(screen, INK, [(x - 80, cap_y - 58), (x, cap_y - 94), (x + 80, cap_y - 58), (x, cap_y - 30)])
    pygame.draw.ellipse(screen, INK, (x - 42, cap_y - 62, 84, 30))
    swing = math.sin(s * (8 if mood == "happy" else 3)) * (9 if mood == "happy" else 4)
    tx = x + 74 + swing
    pygame.draw.line(screen, GOLD, (x + 66, cap_y - 58), (tx, cap_y - 20), 4)
    pygame.draw.circle(screen, GOLD, (int(tx), int(cap_y - 17)), 7)

    # sparkles when happy
    if mood == "happy":
        for i in range(3):
            a = s * 2 + i * 2.1
            sx, sy = x + math.cos(a) * 120, y - 10 + math.sin(a) * 80
            pygame.draw.polygon(screen, GOLD, [(sx, sy - 9), (sx + 5, sy), (sx, sy + 9), (sx - 5, sy)])


# SCREENS
def draw_header():
    shadow = f_title.render("NGOSOFY", True, GOLD_SOFT)
    screen.blit(shadow, shadow.get_rect(center=(W // 2 + 4, 74)))
    title = f_title.render("NGOSOFY", True, INK)
    screen.blit(title, title.get_rect(center=(W // 2, 70)))
    sub = f_small.render("COMMON SPELLING MISTAKES & CONTEXTUAL ERRORS", True, MUTED)
    screen.blit(sub, sub.get_rect(center=(W // 2, 128)))
    pygame.draw.line(screen, GOLD, (W // 2 - 70, 156), (W // 2 - 14, 156), 4)
    pygame.draw.line(screen, GOLD, (W // 2 + 14, 156), (W // 2 + 70, 156), 4)
    pygame.draw.circle(screen, GOLD_DARK, (W // 2, 156), 6)


def draw_progress():
    label = f_small.render(f"QUESTION {current + 1} OF {len(questions)}", True, BROWN)
    screen.blit(label, (160, 182))
    sc = f_small.render(f"SCORE: {score}", True, BROWN)
    screen.blit(sc, sc.get_rect(topright=(1440, 182)))
    bar = pygame.Rect(160, 218, 1280, 14)
    pygame.draw.rect(screen, GOLD_SOFT, bar, border_radius=7)
    fill = int(bar.w * progress_anim)
    if fill > 0:
        pygame.draw.rect(screen, GOLD, (bar.x, bar.y, max(fill, 14), bar.h), border_radius=7)


def draw_question(now):
    q = questions[current]
    draw_header()
    draw_progress()

    card = pygame.Rect(140, 270, 1320, 260)
    draw_card(card)
    h = block_height(q['question'], f_q, 1160)
    draw_block(q['question'], f_q, INK, card.centerx, card.centery - h // 2, 1160)

    mouse = pygame.mouse.get_pos()
    for i, rect in enumerate(BUTTONS):
        sel = i == selected
        hover = rect.collidepoint(mouse)
        r = rect.move(0, -6 if (sel or hover) else 0)
        fill = GOLD if sel else (GOLD_SOFT if hover else CARD)
        draw_card(r, fill, INK if sel else GOLD, radius=24)

        badge = (r.x + 56, r.centery)
        pygame.draw.circle(screen, INK if sel else GOLD_SOFT, badge, 28)
        letter = f_badge.render("ABC"[i], True, CARD if sel else BROWN)
        screen.blit(letter, letter.get_rect(center=badge))

        text = q['options'][i]
        tx = r.x + 96 + (r.w - 120) // 2
        th = block_height(text, f_opt, 270)
        draw_block(text, f_opt, INK, tx, r.centery - th // 2, 270)

    if now < warn_until:
        warn = f_small.render("PICK AN ANSWER FIRST", True, RED)
        screen.blit(warn, warn.get_rect(center=(W // 2, 770)))
    hint = f_small.render("ARROW KEYS, MOUSE OR A / B / C TO CHOOSE   |   ENTER TO SUBMIT", True, MUTED)
    screen.blit(hint, hint.get_rect(center=(W // 2, 825)))


def draw_feedback(now):
    q = questions[current]
    t = now - feedback_start
    chosen = q['options'][selected]
    colour = GREEN if was_correct else RED

    draw_header()
    draw_card((120, 200, 1360, 600))

    # banner with check / cross icon
    pygame.draw.circle(screen, colour, (205, 268), 34)
    if was_correct:
        pygame.draw.lines(screen, CARD, False, [(190, 268), (201, 280), (222, 254)], 8)
    else:
        pygame.draw.line(screen, CARD, (192, 255), (218, 281), 8)
        pygame.draw.line(screen, CARD, (218, 255), (192, 281), 8)
    msg = f_banner.render(feedback_msg, True, colour)
    screen.blit(msg, msg.get_rect(midleft=(262, 268)))

    # answer pills
    x = 170
    if not was_correct:
        r = draw_pill(f"You chose: {chosen}", x, 335, RED_SOFT, RED)
        x = r.right + 24
    draw_pill(f"Answer: {q['answer']}", x, 335, GREEN_SOFT, GREEN)

    # speech bubble + tail pointing at Noso
    bubble = pygame.Rect(170, 430, 900, 290)
    draw_card(bubble, BUBBLE, GOLD_SOFT, radius=28, shadow=False)
    pygame.draw.polygon(screen, BUBBLE, [(1064, 535), (1064, 595), (1124, 570)])
    pygame.draw.lines(screen, GOLD_SOFT, False, [(1068, 535), (1124, 570), (1068, 595)], 3)

    title = f_small.render("NOSO EXPLAINS", True, GOLD_DARK)
    screen.blit(title, (210, 458))
    chars = max(0, int((now - type_start) / 1000 * TYPE_SPEED))
    draw_block(q['explanation'], f_body, INK, 210, 510, 820, center=False, chars=chars)

    # Noso slides in from the right, then reacts
    slide = (1 - ease_out(min(1, t / 450))) * 360
    draw_noso(1290 + slide, 470, "happy" if was_correct else "sad", t)
    name = f_small.render("NOSO", True, BROWN)
    screen.blit(name, name.get_rect(center=(1290 + slide, 735)))

    done = chars >= len(q['explanation'])
    hint = "PRESS ENTER TO CONTINUE" if done else "PRESS ENTER TO SKIP AHEAD"
    h = f_small.render(hint, True, MUTED)
    screen.blit(h, h.get_rect(center=(W // 2, 838)))


def draw_final(now):
    t = now - final_start
    pct = score / len(questions)
    draw_header()
    draw_card((150, 200, 1300, 600))

    cx = 640
    title = f_banner.render("Game Completed!", True, INK)
    screen.blit(title, title.get_rect(center=(cx, 275)))

    stars = 3 if pct >= 0.9 else 2 if pct >= 0.65 else 1 if pct >= 0.35 else 0
    for i in range(3):
        bob = math.sin(t / 300 + i) * 4 if i < stars else 0
        draw_star(cx - 110 + i * 110, 365 + bob, 46, GOLD if i < stars else GOLD_SOFT)

    lbl = f_small.render("YOUR SCORE", True, MUTED)
    screen.blit(lbl, lbl.get_rect(center=(cx, 450)))
    big = f_big.render(f"{score} / {len(questions)}", True, INK)
    screen.blit(big, big.get_rect(center=(cx, 535)))

    if pct == 1:
        message, col = "Perfect score! Brilliant work!", GREEN
    elif pct >= 0.5:
        message, col = "Great work! Keep learning!", GREEN
    else:
        message, col = "Keep practising, you'll improve!", RED
    m = f_opt.render(message, True, col)
    screen.blit(m, m.get_rect(center=(cx, 640)))

    slide = (1 - ease_out(min(1, t / 450))) * 300
    draw_noso(1180 + slide, 440, "happy" if pct >= 0.5 else "sad", t)
    name = f_small.render("NOSO", True, BROWN)
    screen.blit(name, name.get_rect(center=(1180 + slide, 705)))

    h = f_small.render("PRESS ENTER TO PLAY AGAIN", True, MUTED)
    screen.blit(h, h.get_rect(center=(W // 2, 838)))


# GAME ACTIONS
def start_fade(now):
    global fade_start
    fade_start = now


def submit(now):
    global state, score, was_correct, feedback_msg, feedback_start, type_start, warn_until
    if selected == -1:
        warn_until = now + 1600
        return
    q = questions[current]
    was_correct = q['options'][selected] == q['answer']
    if was_correct:
        score += 1
        spawn_confetti()
    feedback_msg = random.choice(GOOD_MSGS if was_correct else BAD_MSGS)
    feedback_start = now
    type_start = now + 450
    state = "feedback"
    start_fade(now)


def advance(now):
    global state, current, selected, final_start
    if current < len(questions) - 1:
        current += 1
        selected = -1
        state = "question"
    else:
        state = "final"
        final_start = now
        if score / len(questions) >= 0.5:
            spawn_confetti(140, 640, 330)
    start_fade(now)


def restart(now):
    global state, current, score, selected, progress_anim
    state, current, score, selected, progress_anim = "question", 0, 0, -1, 0.0
    confetti.clear()
    start_fade(now)


def handle_key(key, now):
    global selected, type_start
    enter = key in (pygame.K_RETURN, pygame.K_KP_ENTER)
    if state == "question":
        if key in (pygame.K_RIGHT, pygame.K_DOWN):
            selected = 0 if selected == -1 else (selected + 1) % 3
        elif key in (pygame.K_LEFT, pygame.K_UP):
            selected = 2 if selected == -1 else (selected - 1) % 3
        elif key in KEY_CHOICES:
            selected = KEY_CHOICES[key]
        elif enter:
            submit(now)
    elif state == "feedback" and enter:
        full = int(len(questions[current]['explanation']) / TYPE_SPEED * 1000) + 50
        if now - type_start < full:
            type_start = now - 10 ** 6      # first Enter finishes the typing
        else:
            advance(now)
    elif state == "final" and enter:
        restart(now)


# MAIN LOOP
while running:
    dt = clock.tick(60) / 1000
    now = pygame.time.get_ticks()
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                handle_key(event.key, now)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and state == "question":
            for i, rect in enumerate(BUTTONS):
                if rect.collidepoint(event.pos):
                    selected = i

    target = (current + (1 if state != "question" else 0)) / len(questions)
    progress_anim += (target - progress_anim) * min(1, dt * 6)

    if state == "question":
        draw_question(now)
    elif state == "feedback":
        draw_feedback(now)
    else:
        draw_final(now)

    update_confetti(dt)
    draw_confetti()

    e = now - fade_start
    if e < 300:
        fade_surface.set_alpha(int(255 * (1 - e / 300)))
        screen.blit(fade_surface, (0, 0))

    pygame.display.flip()

pygame.quit()