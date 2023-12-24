import curses
import random

# Initialize the curses library
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# Set up the game field
field_width = 20
field_height = 10
field = [[' ' for _ in range(field_width)] for _ in range(field_height)]

# Create the snake
snake = [(field_height // 2, field_width // 2)]
direction = curses.KEY_RIGHT

# Create the food
food = (random.randint(0, field_height - 1), random.randint(0, field_width - 1))

# Main game loop
while True:
    # Get user input
    key = stdscr.getch()

    # Update the snake's direction
    if key == curses.KEY_UP and direction != curses.KEY_DOWN:
        direction = curses.KEY_UP
    elif key == curses.KEY_DOWN and direction != curses.KEY_UP:
        direction = curses.KEY_DOWN
    elif key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
        direction = curses.KEY_LEFT
    elif key == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
        direction = curses.KEY_RIGHT
    elif key == ord('q'):
        break

    # Update the snake's position
    head = snake[0]
    if direction == curses.KEY_UP:
        head = (head[0] - 1, head[1])
    elif direction == curses.KEY_DOWN:
        head = (head[0] + 1, head[1])
    elif direction == curses.KEY_LEFT:
        head = (head[0], head[1] - 1)
    elif direction == curses.KEY_RIGHT:
        head = (head[0], head[1] + 1)

    # Check if the snake has eaten the food
    if head == food:
        # Increase the snake's length
        snake.append(snake[-1])

        # Create a new piece of food
        food = (random.randint(0, field_height - 1), random.randint(0, field_width - 1))

    # Check if the snake has hit itself or the wall
    if head in snake[1:] or head[0] < 0 or head[0] >= field_height or head[1] < 0 or head[1] >= field_width:
        break

    # Update the field
    for i in range(field_height):
        for j in range(field_width):
            if (i, j) in snake:
                field[i][j] = '█'
            elif (i, j) == food:
                field[i][j] = 'o'
            else:
                field[i][j] = ' '

    # Draw the field
    stdscr.clear()
    for i in range(field_height):
        for j in range(field_width):
            stdscr.addstr(i, j, field[i][j])

    stdscr.refresh()

# Game over
stdscr.addstr(field_height // 2, field_width // 2 - 4, "Game Over")
stdscr.refresh()
stdscr.getch()

# End the curses library
curses.endwin()