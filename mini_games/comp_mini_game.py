import pygame
import random
import time
import subprocess
import json

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Computer Tasks")

# Load background image
background_image = pygame.image.load("assets/background/computer_screen.jpeg")  # Replace with your image file path
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Scale image to fit the screen

# Define colors
BAR = (25, 32, 55)
FRAME = (135, 141, 153)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Font settings
font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 48)

# Game variables
words = ["apple", "banana", "cherry", "date", "elephant", "giraffe", "honey", "ice", "jaguar", "kite", "lemon", "monkey"]
word_speed = 1  # Speed for the words falling down
input_text = ''
score = 0
start_time = time.time()

# Variable to track the current word and its position
current_word = None
word_y_position = 0
spacing_between_words = 80  # Distance between words (increased for clarity)

instructions = "Type the falling words to score points! Press Enter to submit. Need a 70 to Pass!"

# Function to wrap text
def wrap_text(text, font, width):
    words = text.split(' ')
    lines = []
    current_line = words[0]
    
    for word in words[1:]:
        # Check if adding the word would exceed the width
        if font.size(current_line + ' ' + word)[0] <= width:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)  # Add the last line
    return lines

# Function to draw the "Check on Classroom" button
def draw_button():
    button_text = "Check on Class"
    button_surface = font.render(button_text, True, BAR)
    button_width, button_height = button_surface.get_size()
    button_x = 10  # Position the button on the left
    button_y = HEIGHT - button_height - 10  # Position the button at the bottom

    # Draw the button rectangle
    pygame.draw.rect(screen, WHITE, (button_x - 10, button_y - 10, button_width + 20, button_height + 20))  # Add padding around button
    screen.blit(button_surface, (button_x, button_y))  # Draw the button text

    return pygame.Rect(button_x - 10, button_y - 10, button_width + 20, button_height + 20)  # Return button rect for click detection

# Save the score to a JSON file
def save_score(score):
    data = {"score": score}
    with open("jsons/comp_mini_game_data.json", "w") as file:
        json.dump(data, file)

# Game loop
running = True
while running:
    # Draw the background image first
    screen.blit(background_image, (0, 0))

    
    # Wrap the instructions text
    instruction_lines = wrap_text(instructions, font, WIDTH - 20)
    # Calculate the height of the instruction bar based on the number of lines
    instruction_bar_height = len(instruction_lines) * 40 + 20  # 40px per line, 20px padding
    # Draw the instruction bar at the top
    pygame.draw.rect(screen, FRAME, (0, 0, WIDTH, instruction_bar_height))  # Instruction bar
    
    # Draw the wrapped instructions text
    for i, line in enumerate(instruction_lines):
        instruction_text = font.render(line, True, WHITE)
        screen.blit(instruction_text, (10, 10 + i * 40))  # Position each line with a 40-pixel gap
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif event.key == pygame.K_RETURN:
                # Check if the input matches the word
                if current_word and input_text == current_word[0]:
                    score += 10  # Increase score by 10 for each correct word typed
                    current_word = None  # Reset current word after it is typed correctly
                input_text = ''
            else:
                input_text += event.unicode

    # Add a new word to the list at random intervals, ensuring only one word falls at a time
    if current_word is None:
        # current_word = [random.choice(words), 0]  # Add a new word with the starting y position fixed at 0
        current_word = [random.choice(words), instruction_bar_height]  # Start word below the instruction bar

    # Draw the word falling down
    if current_word:
        word, pos = current_word
        word_surface = font.render(word, True, BLACK)
        screen.blit(word_surface, (WIDTH // 2 - word_surface.get_width() // 2, pos))

        # Update the word's position (make it fall down)
        current_word = (word, pos + word_speed)

        # Remove the word if it has passed the screen
        if current_word[1] >= HEIGHT:
            current_word = None  # Reset current word after it falls off the screen

    # Draw a line between the words and the input field
    line_y = HEIGHT - 60  # Position of the line
    pygame.draw.line(screen, BLACK, (0, line_y), (WIDTH, line_y), 2)

    # Fill the area below the line with the bar color
    pygame.draw.rect(screen, BAR, (0, line_y, WIDTH, HEIGHT - line_y))

    # Display the score
    score_text = font.render(f"Grade: {score}", True, WHITE)
    score_rect = score_text.get_rect(topleft=(10, instruction_bar_height + 10))

    # Draw a rectangle behind the score text with the BAR color
    score_rect = pygame.draw.rect(screen, BAR, score_rect.inflate(20, 10))  # Add some padding around the score
    screen.blit(score_text, score_rect)

    # Display the user's input
    input_surface = input_font.render(input_text, True, WHITE)
    screen.blit(input_surface, (WIDTH // 2 - input_surface.get_width() // 2, HEIGHT - 50))

    # Check for passing condition
    if score >= 70:
        # Show pass message
        pass_text = font.render("You Passed!", True, GREEN)
        screen.blit(pass_text, (WIDTH // 2 - pass_text.get_width() // 2, HEIGHT // 2))

    # Draw the "Check on Classroom" button
    button_rect = draw_button()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if button_rect.collidepoint(event.pos):  # Button clicked
            save_score(score)  # Save score to JSON
            subprocess.run(["python", "game101.py"])  # Go back to game101.py

    # Update the screen
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)

# Quit the game
pygame.quit()
