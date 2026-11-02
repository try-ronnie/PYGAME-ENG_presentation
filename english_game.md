# ENGLIFICATION — Simple English Pygame Game

A small pygame project that teaches users which words to use depending on context and common spelling errors, through user input.

## Project structure

```
PYGAME/
├── english_game.md          # This guide
├── Pipfile
└── basics/
    ├── Game.py              # Minimal pygame window + event loop
    ├── exe_1.py             # Rectangles + mouse click detection (collidepoint)
    ├── text.py              # Text rendering, fonts, blitting, shapes
    ├── rect.py              # Rect creation + keyboard and mouse events
    ├── key_handling.py      # KEYDOWN / KEYUP arrow key handling
    └── dsa_game_logic.py    # Questions stored as list of dictionaries
```

## 1. Pygame basics

### Initialize and create a window

```python
import pygame, sys

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ENGLIFICATION')
```

- `pygame.init()` — initializes all imported pygame modules.
- `pygame.display.set_mode((width, height))` — creates the display surface.
- `pygame.display.set_caption(title)` — sets the window title.

### Colours

Colours are RGB tuples:

```python
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
black  = (0, 0, 0)
```

## 2. The game loop

Every pygame program repeats this cycle:

```python
running = True

while running:
    # 1. Handle events (input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update game state
    # ...

    # 3. Draw everything
    DISPLAYSURF.fill(white)          # clear the screen
    # pygame.draw... / DISPLAYSURF.blit(...)

    # 4. Refresh the display
    pygame.display.flip()
```

| Step | Purpose |
|------|---------|
| Event loop | Processes pending events from the event queue (quit, keys, mouse). |
| Update | Changes game state (positions, scores, current question). |
| Draw | Renders shapes, text, and images onto the surface. |
| `flip()` | Updates the entire display surface to the screen. |

`pygame.display.flip()` must be called every frame, even when nothing changed; otherwise rendering becomes tied to user input and the screen may appear frozen.

### Event types vs input loops

- The `while` loop repeats the **entire game cycle**.
- The `for event in pygame.event.get()` loop only processes events **waiting in the queue**.

## 3. Events — keyboard and mouse input

### Event types

| Event type | Meaning |
|------------|---------|
| `pygame.QUIT` | User closed the window. |
| `pygame.KEYDOWN` / `pygame.KEYUP` | A key was pressed / released. |
| `pygame.MOUSEBUTTONDOWN` | A mouse button was clicked. |

### Keyboard

```python
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_DOWN:
        print('down pressed')
    elif event.key == pygame.K_UP:
        print('up pressed')
    elif event.key == pygame.K_LEFT:
        print('left pressed')
    elif event.key == pygame.K_RIGHT:
        print('right pressed')
```

Arrow keys: `K_DOWN`, `K_UP`, `K_LEFT`, `K_RIGHT`.

### Mouse

```python
if event.type == pygame.MOUSEBUTTONDOWN:
    if event.button == 1:          # left click
        print(event.pos)           # (x, y) position of the click
```

Mouse buttons: `1` left, `2` middle, `3` right, `4` scroll up, `5` scroll down.  
`event.pos` gives the click position as a tuple `(x, y)`.

See `basics/key_handling.py` and `basics/rect.py` for working examples.

## 4. Drawing shapes

`pygame.Rect(x, y, width, height)` defines a rectangle starting at `(x, y)`.

```python
rect = pygame.Rect(100, 200, 100, 100)   # x=100, y=200, w=100, h=100
```

Common drawing functions (all take `surface` as first argument):

```python
pygame.draw.rect(DISPLAYSURF, red, rect)                 # rectangle
pygame.draw.circle(DISPLAYSURF, yellow, (100, 600), 50)  # circle
pygame.draw.line(DISPLAYSURF, colour, start_point, end_point)
pygame.draw.polygon(DISPLAYSURF, colour, points, width)
```

Rect `width` behaviour:
- `width == 0` → filled rectangle
- `width > 0` → line thickness
- `width < 0` → draws nothing

See `basics/exe_1.py` and `basics/text.py` for drawing examples.

## 5. Rects and click detection

Rects have helper methods, the most useful being `collidepoint(point)`:

```python
answer_rect = pygame.Rect(200, 300, 400, 400)

if event.button == 1 and answer_rect.collidepoint(event.pos):
    print('rectangle has been clicked')
else:
    print('somewhere else is clicked')
```

`collidepoint(event.pos)` returns `True` when the click position falls inside the rectangle.

See `basics/exe_1.py` and `basics/text.py`.

## 6. Rendering text

### Create a font

```python
font = pygame.font.Font(None, 38)   # font file path (None = default), size
```

Pygame has no native fonts; pass a `.ttf`/`.otf` file path or `None` for the default.

### Render text to a surface

```python
text = font.render('answer a', True, green)   # text, antialias, colour
```

This returns a new surface containing the rendered text.

### Place text on screen

```python
text_rect = text.get_rect(center = rect1.center)   # position the text
DISPLAYSURF.blit(text, text_rect)                  # draw text surface onto display
```

`blit(source, dest)` draws one surface onto another at the given position.

Full example (`basics/text.py`):

```python
DISPLAYSURF.fill(white)
pygame.draw.rect(DISPLAYSURF, red, rect1)
pygame.draw.rect(DISPLAYSURF, blue, rect2)
pygame.draw.rect(DISPLAYSURF, green, rect3)
pygame.draw.circle(DISPLAYSURF, yellow, (100, 600), 50)

DISPLAYSURF.blit(text1, text1_rect)
DISPLAYSURF.blit(text2, text2_rect)
DISPLAYSURF.blit(text3, text3_rect)
pygame.display.flip()
```

## 7. Game data — questions and answers

`basics/dsa_game_logic.py` stores questions as a list of dictionaries:

```python
current_question = 0

questions = [
    {
        'question': 'Kate went to the pet store to buy a ?',
        'options': ['beach', 'bitch'],
        'answer': 'bitch',
    },
    {
        'question': "i need your ____ on this matter",
        'options': ['advice', 'advise'],
        'answer': 'advice',
    },
]
```

Keep question text, options, and the correct answer together so the game can look them up by `current_question`.

## 8. File-by-file summary

| File | What it demonstrates |
|------|----------------------|
| `basics/Game.py` | Minimal window, init, quit event loop |
| `basics/exe_1.py` | Rectangles, colours, `collidepoint`, mouse clicks |
| `basics/text.py` | Fonts, `render`, `blit`, shapes, multiple click targets |
| `basics/rect.py` | `pygame.Rect`, keyboard + mouse events, `event.pos` |
| `basics/key_handling.py` | `KEYDOWN` / `KEYUP`, arrow keys |
| `basics/dsa_game_logic.py` | Question data as list of dictionaries |

## 9. Quick checklist

- [ ] Call `pygame.init()` before anything else.
- [ ] Create the display surface with `set_mode`.
- [ ] Run a `while running:` loop with an inner `for event in pygame.event.get():`.
- [ ] Handle `pygame.QUIT` to set `running = False`.
- [ ] Clear the screen each frame with `DISPLAYSURF.fill(colour)`.
- [ ] Draw shapes / blit text.
- [ ] Call `pygame.display.flip()` every frame.
- [ ] Use `collidepoint(event.pos)` for click detection on rects.
- [ ] Use `font.render()` + `get_rect()` + `blit()` for text.
