import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600  # Window size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Splash Screen")

# Load the splash screen background image
background = pygame.image.load("assets/background/start_screen.png")
background = pygame.transform.scale(background, (width, height))

# Define the start button
button_width = 200
button_height = 50
start_button_x = (width - button_width) - 80 # Position the button near the right edge
start_button_y = (height - button_height) // 2 + 90  # Center the button vertically
start_button_rect = pygame.Rect(start_button_x, start_button_y, button_width, button_height)
start_button_font_color = (255, 255, 255)
start_button_background = (102,133,103)

# Load fonts
font = pygame.font.Font(None, 36)

# Function to create a button
def create_button(text, rect, color, text_color):
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (rect.x + (rect.width - text_surface.get_width()) // 2, rect.y + (rect.height - text_surface.get_height()) // 2))

# Main loop for the splash screen
def splash_screen():
    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))  # Display the background

        # Draw the "Start" button
        create_button("Start", start_button_rect, start_button_background, start_button_font_color)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    # Quit Pygame and close splash screen before launching game101
                    pygame.quit()
                    running = False  # Exit the splash screen loop
                    
                    # Start the game by running game101.py in a separate process
                    subprocess.Popen(["python", "game101.py"])
                    break
        
        pygame.display.flip()

# Run the splash screen
splash_screen()