import pygame
import sys

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
#student tables:
table_1 = pygame.Rect(100, 250, 125, 100)  # Table 1, Row 1
table_2 = pygame.Rect(265, 250, 125, 100)  # Table 2, Row 1
table_3 = pygame.Rect(420, 250, 125, 100)  # Table 3, Row 1
table_4 = pygame.Rect(580, 250, 125, 100)  # Table 4, Row 1

table_5 = pygame.Rect(100, 370, 125, 100)  # Table 4, Row 2
table_6 = pygame.Rect(265, 370, 125, 100)  # Table 5, Row 2
table_7 = pygame.Rect(420, 370, 125, 100)  # Table 6, Row 2
table_8 = pygame.Rect(580, 370, 125, 100)  # Table 4, Row 2

student_tables = [table_1, table_2, table_3, table_4, table_5, table_6, table_7, table_8]

#classroom task tables
class_table_1 = pygame.Rect(95, 470, 125, 100)  # Table 1 (bottom left computer)
class_table_2 = pygame.Rect(260, 470, 125, 100)  # Table 2 (bottom left student)
class_table_3 = pygame.Rect(425, 470, 125, 100)  # Table 3 (bottom right student)
class_table_4 = pygame.Rect(305, 120, 200, 125)  # Table 4 (teacher table)
class_table_5 = pygame.Rect(515, 100, 80, 100)  # Table 5 (Orange chair)

task_tables = [class_table_1, class_table_2, class_table_3, class_table_4, class_table_5]

# Function to switch to a different screen (just a placeholder here)
def go_to_next_screen(table_number):
    print(f"You clicked on Table {table_number}! Switching screens...")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Check student tables
            for i, table in enumerate(student_tables, start=1):
                if table.collidepoint(mouse_pos):
                    go_to_next_screen(i)
                    break

            # Check task tables
            for j, table in enumerate(task_tables, start=9):  # Continue numbering from 9
                if table.collidepoint(mouse_pos):
                    go_to_next_screen(j)
                    break

    # Draw the background image
    screen.blit(background, (0, 0))

    # Draw clickable tables (optional: just for visual reference)
    for table in student_tables:
        pygame.draw.rect(screen, (255, 0, 0), table, 2)  # Red outline for tables

    # Draw outlines for task tables (blue)
    for table in task_tables:
        pygame.draw.rect(screen, (0, 0, 255), table, 2)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
