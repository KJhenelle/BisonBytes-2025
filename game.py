import pygame
import sys
import random
from scenario import popscene1
from math_mini_game import run_math_game
from read_mini_game import run_read_game

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600  # Window size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Classroom Game")

# Load the background image
background = pygame.image.load("assets/background/classroom_chaos_main_background.png")
background = background.convert()

# Scale the background image to fit the window
background = pygame.transform.scale(background, (width, height))

# Define clickable areas (tables) based on the screenshot positions
# Student tables:
table_1 = pygame.Rect(100, 250, 125, 100)  # Table 1, Row 1
table_2 = pygame.Rect(265, 250, 125, 100)  # Table 2, Row 1
table_3 = pygame.Rect(420, 250, 125, 100)  # Table 3, Row 1
table_4 = pygame.Rect(580, 250, 125, 100)  # Table 4, Row 1

table_5 = pygame.Rect(100, 370, 125, 100)  # Table 4, Row 2
table_6 = pygame.Rect(265, 370, 125, 100)  # Table 5, Row 2
table_7 = pygame.Rect(420, 370, 125, 100)  # Table 6, Row 2
table_8 = pygame.Rect(580, 370, 125, 100)  # Table 4, Row 2

student_tables = [table_1, table_2, table_3, table_4, table_5, table_6, table_7, table_8]

# Classroom task tables
class_table_1 = pygame.Rect(95, 470, 125, 100)  # Table 1 (bottom left computer)
class_table_2 = pygame.Rect(260, 470, 125, 100)  # Table 2 (bottom left student)
class_table_3 = pygame.Rect(425, 470, 125, 100)  # Table 3 (bottom right student)
class_table_4 = pygame.Rect(305, 120, 200, 125)  # Table 4 (teacher table)
class_table_5 = pygame.Rect(515, 100, 80, 100)  # Table 5 (Orange chair)

task_tables = [class_table_1, class_table_2, class_table_3, class_table_4, class_table_5]

# Table states (list of dictionaries)
table_states = [
    {"rect": table, "clickable": False, "timer": 0, "sprite_index": 4, "cooldown": 0}
    for table in student_tables + task_tables
]

# Load the timer sprites
timer_sprites = [
    pygame.image.load(f"assets/background/sprite_{i}.png").convert_alpha() for i in range(5)
]

# Function to wrap text so it doesn't run off the screen
def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + " " + word if current_line else word
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

# Function to display the scenario and options
def show_scenario_screen(scenario, options, table_number):
    if not scenario:  # If no scenario is available
        # Display a message on the original screen
        font = pygame.font.Font(None, 36)
        no_scenario_text = font.render("No scenario available", True, (255, 255, 255))  # White text
        screen.blit(background, (0, 0))  # Draw the original background
        screen.blit(no_scenario_text, (50, 50))  # Display the message
        pygame.display.flip()

        # Wait for a short time (e.g., 2 seconds) before returning to the main screen
        pygame.time.delay(2000)
        return

    # If a scenario is available, proceed as before
    screen.fill((255, 255, 255))  # Clear screen with white background
    font = pygame.font.Font(None, 36)

    # Wrap the scenario text
    scenario_lines = wrap_text(scenario, font, width - 100)  # Leave 50px margin on each side
    y_offset = 50  # Starting Y position for the scenario text

    # Display the scenario text
    for line in scenario_lines:
        scenario_text = font.render(line, True, (0, 0, 0))  # Black text
        screen.blit(scenario_text, (50, y_offset))
        y_offset += 30  # Move down for the next line

    # Display the options with visible outlines
    option_rects = []
    for i, option in enumerate(options):
        # Wrap the option text
        option_lines = wrap_text(option, font, width - 100)
        for j, line in enumerate(option_lines):
            option_text = font.render(line, True, (0, 0, 0))  # Black text
            option_rect = option_text.get_rect(topleft=(50, y_offset + j * 30))
            screen.blit(option_text, option_rect)
        # Create a clickable area for the entire option
        option_rect = pygame.Rect(50, y_offset, width - 100, len(option_lines) * 30)
        pygame.draw.rect(screen, (0, 0, 255), option_rect, 2)  # Blue outline for visibility
        option_rects.append(option_rect)
        y_offset += len(option_lines) * 30 + 20  # Add spacing between options

    pygame.display.flip()

    # Wait for user input
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(mouse_pos):
                        print(f"Selected {options[i]} for Table {table_number}")
                        waiting_for_input = False  # Exit the inner loop
                        break  # Exit the for loop
                break  # Exit the event loop to prevent double-click issue

# Function to switch to a different screen
def go_to_next_screen(table_number):
    print(f"You clicked on Table {table_number}!")

    if table_number == 10:  # class_table_2
        run_math_game(screen, width, height)
    else:
        runs1 = random.randint(1, 8)
        scenario, options = popscene1(runs1)
        show_scenario_screen(scenario, options, table_number)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    dt = clock.tick(60) / 1000  # Delta time in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Check student tables
            for i, state in enumerate(table_states[:8], start=1):
                if state["rect"].collidepoint(mouse_pos) and state["clickable"]:
                    go_to_next_screen(i)
                    state["clickable"] = False  # Make the table non-clickable
                    state["timer"] = 0  # Reset the timer
                    state["sprite_index"] = 4  # Reset the sprite index to unclickable
                    state["cooldown"] = 5  # Start cooldown period (5 seconds)
                    break

            # Check task tables
            for j, state in enumerate(table_states[8:], start=9):  # Continue numbering from 9
                if state["rect"].collidepoint(mouse_pos) and state["clickable"]:
                    go_to_next_screen(j)
                    state["clickable"] = False  # Make the table non-clickable
                    state["timer"] = 0  # Reset the timer
                    state["sprite_index"] = 4  # Reset the sprite index to unclickable
                    state["cooldown"] = 5  # Start cooldown period (5 seconds)
                    break

    # Update table states
    for state in table_states:
        if state["cooldown"] > 0:
            # Cooldown period: no sprite is displayed, and the table is unclickable
            state["cooldown"] -= dt
            if state["cooldown"] <= 0:
                state["cooldown"] = 0  # End cooldown
        elif state["clickable"]:
            # Update the timer during the sprite cycle
            state["timer"] += dt
            if state["timer"] >= 5:  # 5 seconds per sprite
                state["timer"] = 0
                state["sprite_index"] += 1  # Move to the next sprite

                # If the sprite index reaches 4, start cooldown
                if state["sprite_index"] >= 4:
                    state["clickable"] = False
                    state["sprite_index"] = 4  # Keep the sprite at index 4
                    state["cooldown"] = 5  # Start cooldown period (5 seconds)
        else:
            # Randomly make a table clickable (only for student tables)
            if state["rect"] in student_tables and random.random() < 0.01:  # 1% chance per frame
                state["clickable"] = True
                state["timer"] = 0
                state["sprite_index"] = 0  # Start with sprite_0

    # Draw the background image
    screen.blit(background, (0, 0))

    # Draw tables with appropriate sprites (only for student tables)
    for state in table_states:
        if state["rect"] in student_tables:
            if state["cooldown"] > 0:
                # Cooldown period: no sprite is displayed
                pass
            elif state["clickable"]:
                # Display the current sprite (sprite_0, sprite_1, sprite_2, or sprite_3)
                if state["sprite_index"] < 4:
                    screen.blit(timer_sprites[state["sprite_index"]], state["rect"].topleft)
            else:
                # Display sprite_4 (unclickable)
                if state["sprite_index"] == 4:
                    screen.blit(timer_sprites[4], state["rect"].topleft)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()