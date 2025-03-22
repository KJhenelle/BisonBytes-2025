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

# Scale the background image to fit the window
background = pygame.transform.scale(background, (width, height))

# Define clickable areas (tables) based on the screenshot positions
student_tables = [
    pygame.Rect(100, 250, 125, 100),  # Table 1 (Green chair)

    pygame.Rect(350, 150, 125, 100),  # Table 2 (Green chair)


    pygame.Rect(500, 150, 100, 100),  # Table 3 (Blue chair)

    pygame.Rect(200, 300, 100, 100),  # Table 4 (Orange chair)
    pygame.Rect(350, 300, 100, 100),  # Table 5 (Orange chair)
    pygame.Rect(500, 300, 100, 100),  # Table 6 (Orange chair)
]

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
            for i, table in enumerate(tables, start=1):  # Start counting tables from 1
                if table.collidepoint(mouse_pos):
                    go_to_next_screen(i)  # Trigger action for the clicked table
                    break  # Stop checking other tables once one is clicked

    # Draw the background image
    screen.blit(background, (0, 0))

    # Draw clickable tables (optional: just for visual reference)
    for table in tables:
        pygame.draw.rect(screen, (255, 0, 0), table, 2)  # Red outline for tables

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
