# start_screen.py
import pygame
import sys
# from typing_game import run_typing_game  # Import your game function

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Game - Start Screen")

# Load assets
start_bg = pygame.image.load("assets/background/start_screen.png").convert()
start_bg = pygame.transform.scale(start_bg, (WIDTH, HEIGHT))

# Button properties (adjust these coordinates to match your image)
START_BUTTON = {
    "rect": pygame.Rect(250, 380, 300, 80),  # x, y, width, height
    "color": (255, 255, 255),
    "hover_color": (200, 200, 200)
}

def draw_button(button, mouse_pos):
    # Draw button with hover effect
    color = button["hover_color"] if button["rect"].collidepoint(mouse_pos) else button["color"]
    pygame.draw.rect(screen, color, button["rect"], border_radius=15)

def start_screen():
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON["rect"].collidepoint(mouse_pos):
                    run_typing_game(screen, WIDTH, HEIGHT)  # Launch the game
                    pygame.display.set_caption("Typing Game - Start Screen")  # Restore caption

        # Drawing
        screen.blit(start_bg, (0, 0))
        draw_button(START_BUTTON, mouse_pos)
        
        # Add button text
        font = pygame.font.Font(None, 50)
        text = font.render("Start Typing", True, (0, 0, 0))
        text_rect = text.get_rect(center=START_BUTTON["rect"].center)
        screen.blit(text, text_rect)

        pygame.display.flip()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    start_screen()
    pygame.quit()