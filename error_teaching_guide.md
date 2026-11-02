# error.py — Teaching Guide (Extracted Comments)

All comments below were taken from `error.py` and rewritten in a teaching format. The original `error.py` file has been cleaned of all comments — only the executable code remains.

---

## 1. Questions That Run the Game

### What you're looking at

`questions` is a **list of dictionaries**. Each dictionary represents one question in the game.

```python
questions = [
    {'q_no': 0, 'question': "...", 'options': [...], 'answer': '...', 'explanation': '...'},
    ...
]
```

### What each key means

| Key | Purpose |
|-----|---------|
| `q_no` | The question number (used to track position). |
| `question` | The sentence displayed to the player with a blank to fill. |
| `options` | A list of three possible answers (only one is correct). |
| `answer` | The correct answer string used to check the player's choice. |
| `explanation` | A short explanation shown after answering (teaches *why* it's correct). |

### Teaching point: why dictionaries?

Grouping related data (question, options, answer, explanation) into one dictionary keeps everything about a single question together. You access it with `questions[current_question]`, which gives you the whole question block at once.

---

## 2. Additional Variables (Game State)

These variables track the overall progress and state of the game.

### `current_question`

```python
current_question = 0
```

Keeps track of the question currently being displayed. Python starts counting list positions from zero, so `current_question = 0` means the **first** question.

### `score`

```python
score = 0
```

Stores the player's total score. Every time the player selects a correct answer, this value increases by one.

### `selected_option`

```python
selected_option = -1
```

Stores the index of the option currently selected by the player. The three buttons have indexes `0`, `1`, and `2`.

We use `-1` to indicate the player has not selected anything yet. This prevents the first button from automatically being highlighted gold before the player chooses.

### `answered`

```python
answered = False
```

Tracks whether the player has submitted an answer to the current question.

- `False` = question has not been answered yet.
- `True` = player has already submitted an answer.

This prevents the player from repeatedly pressing ENTER and increasing their score multiple times for the same question.

---

## 3. Screen Measurements

```python
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
```

Defines the width and height of the Pygame display. Keeping measurements in variables makes it easier to adjust the screen size later without hunting through the code.

---

## 4. Initialize the Library

```python
pygame.init()
```

`pygame.init()` initializes all the Pygame modules the game needs. This **must** be called before creating the display, fonts, or other Pygame objects.

---

## 5. Create the Display Surface

```python
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('NGOSOFY')
```

- `set_mode()` creates the actual game window. Width and height are passed as a tuple.
- `DISPLAYSURF` is the surface on which everything in the game is drawn.
- `set_caption()` sets the name shown at the top of the game window.

---

## 6. Colour Variables

Pygame represents colours using **RGB** (Red, Green, Blue). Each component is normally a value between 0 and 255.

```python
white   = (255, 255, 255)
black   = (0, 0, 0)
brown   = (101, 67, 33)
dark_brown = (65, 42, 24)
beige   = (245, 237, 220)
gold    = (218, 165, 75)
```

---

## 7. Font Objects

```python
title_font    = pygame.font.Font(None, 96)
question_font = pygame.font.Font(None, 58)
option_font   = pygame.font.Font(None, 48)
small_font    = pygame.font.Font(None, 38)
```

`pygame.font.Font()` creates font objects used to render text:
- First argument: `None` means Pygame's default font (you can also pass a `.ttf` file path).
- Second argument: font size.

Separate font objects are created because different parts of the game need different text sizes (title vs question vs options vs subtitle).

---

## 8. Rectangles for the Choices

```python
buttons = [
    pygame.Rect(80, 590, 440, 120),
    pygame.Rect(580, 590, 440, 120),
    pygame.Rect(1080, 590, 440, 120)
]
```

`pygame.Rect()` creates rectangular objects taking four measurements: **X position, Y position, width, height**.

- All three buttons share the same Y position (`590`) so they appear on the same horizontal level.
- They are stored in a **list** so all three buttons can be accessed and manipulated using loops.

---

## 9. Rendering Text Surfaces

`pygame.font.Font()` only creates the font object. To actually display text, you must **render** it into a surface.

Text is centred inside buttons using `get_rect(center=button.center)`, which positions the rendered option text at the exact centre of its corresponding button.

---

## 10. The Game Loop Control

```python
running = True
```

`running` controls whether the game continues executing. As long as it is `True`, the main game loop keeps repeating. When the player closes the window, it changes to `False`.

---

## 11. Function: `draw_wrapped_text()`

Long questions may exceed the available screen width. Instead of letting text run off the screen, this function splits the question into multiple lines.

### Parameters

| Parameter | Meaning |
|-----------|---------|
| `text` | The question or text to display. |
| `font` | The font object used to render the text. |
| `color` | The colour of the text. |
| `surface` | The surface the text will be drawn on. |
| `x, y` | Position where the text is centred. |
| `max_width` | Maximum permitted width of each line. |

### How it works

1. `text.split()` separates the sentence into individual words (split on whitespace by default).
2. An empty list stores completed lines; each line is rendered separately.
3. `current_line` temporarily holds words being added to the current line.
4. For each word, a `test_line` is built by combining the current line with the next word (plus a space so words don't join together).
5. `font.size(test_line)[0]` measures the width of the text. `[0]` retrieves just the width.
6. If the line still fits within `max_width`, the word is accepted into `current_line`.
7. If the word would make the line too wide, the previous completed line is saved to `lines`, and a new line starts with that word.
8. After the loop, the final line is saved so the last group of words is displayed.
9. Each completed line is rendered with `font.render()` (anti-aliasing enabled with `True`), positioned with `get_rect(center=(x, y))`, and drawn with `surface.blit()`.
10. `y` is increased by `font.get_linesize()` after each line so the next line moves downward instead of overlapping.

---

## 12. Function: `draw_question()`

This function draws the entire question screen: title, subtitle, progress counter, question text, and the three answer buttons.

### What it does, step by step

1. **Retrieves the current question dictionary** using `questions[current_question]`. For example, if `current_question = 0`, it retrieves `questions[0]`, giving access to that question's text, options, and answer.
2. **Draws the game title** "NGOSOFY" using `title_font.render()` with smooth text rendering (`True`) and `dark_brown` colour, centred at `(800, 80)`.
3. **Renders a small subtitle** describing the game ("common spelling mistakes and context based errors") using `small_font`, centred at `(800, 145)`.
4. **Renders the question counter** showing progress like `QUESTION : 1 / 13`. `current_question + 1` is used because Python counts from zero but players expect to see question 1 first. `len(questions)` gives the total count.
5. **Draws the actual question** using `draw_wrapped_text()` instead of direct `render()`, because some questions are longer than others.
6. **Draws the answer buttons and their text**:
   - Uses `enumerate()` to loop through buttons while tracking each button's index.
   - If a button's index matches `selected_option`, it is highlighted `gold`; otherwise it stays `brown`.
   - `pygame.draw.rect()` draws the button with `border_radius=20` for rounded corners.
   - The option text is rendered with `option_font` in white and centred on its button using `get_rect(center=button.center)`.

---

## 13. Main Game Loop

```python
while running:
```

This is the main engine that keeps the game running. It continuously checks for player input, updates the screen, and redraws the current question. Without this loop, the Pygame window would open and immediately close.

### Each iteration

1. **Clear the screen** by filling the display surface with the beige background colour. This prevents new drawings from overlapping old ones.
2. **Process events** with `pygame.event.get()`, which retrieves events since the last iteration (keyboard presses, mouse clicks, window closing).

### Event handling

**QUIT** — If the player clicks the close button, Pygame generates a `QUIT` event. `running` is set to `False` so the loop stops.

**KEYDOWN** — Triggered when a key is pressed. `event.key` identifies which key:

- **RIGHT / DOWN**: Move selection forward by one. `selected_option + 1` increases the index, and `% len(buttons)` wraps it around so pressing right on the third button returns to the first. Example: `(2 + 1) % 3 = 0`.
- **LEFT / UP**: Move selection backward by one. The modulo operator also wraps from the first button back to the last.
- **RETURN (Enter)**: Submit the currently highlighted answer. Two checks must pass:
  1. `selected_option != -1` — player has actually selected one of the three answers.
  2. `not answered` — the current question hasn't already been submitted.
  
  If both pass, the chosen answer is retrieved and compared to the correct answer. If they match, `score` increases by one. Then `answered` is set to `True` to prevent repeated submission of the same question.

**MOUSEBUTTONDOWN** — Triggered when a mouse button is pressed. `event.button` identifies which button; `1` is the left mouse button. `event.pos` gives the click coordinates. `collidepoint()` checks whether the click falls inside a button's rectangle. If so, that button's index is stored in `selected_option`, and `draw_question()` highlights it gold.

### After events

Once all events are processed, `draw_question()` is called to display the current screen. Then `pygame.display.flip()` updates the entire display surface, making all drawings visible to the player. Without `flip()`, changes would not appear on screen.

---

## 14. Exiting the Game

```python
pygame.quit()
```

Once `running` becomes `False`, the main loop ends. `pygame.quit()` shuts down the initialized Pygame modules and releases the resources used by the game.

---

## Quick Reference

| Concept | Key takeaway |
|---------|-------------|
| Questions | Stored as a list of dictionaries; each holds question text, options, answer, and explanation. |
| `current_question` | Zero-based index tracking which question is displayed. |
| `selected_option` | Zero-based index of selected button; `-1` means none selected. |
| `answered` | Boolean preventing duplicate submissions. |
| `pygame.Rect(x, y, w, h)` | Defines a rectangle; all buttons share Y for horizontal alignment. |
| `collidepoint(pos)` | Returns True if a position falls inside a rect — used for click detection. |
| `font.render(text, antialias, color)` | Turns text into a drawable surface. |
| `surface.blit(source, dest)` | Draws one surface onto another. |
| `pygame.display.flip()` | Updates the display every frame. |
| `pygame.init()` / `pygame.quit()` | Initialize and shut down Pygame modules. |
