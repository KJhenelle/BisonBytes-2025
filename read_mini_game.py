import pygame
import random
import requests

# WordsAPI details (sign up for an API key at https://www.wordsapi.com/)
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://wordsapiv1.p.rapidapi.com/words/'

# Function to generate random letters
def generate_letters():
    letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 3)  # 3 random letters for simplicity
    return letters

# Function to check if the word is valid via WordsAPI
def is_valid_word(word):
    word = word.lower()
    url = f"{BASE_URL}{word}/definitions"
    headers = {
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
        "X-RapidAPI-Key": API_KEY
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200 and len(response.json().get('definitions', [])) > 0:
        return True
    else:
        return False

# Function to check if the input word is valid
def check_word(input_word, letters):
    input_word = input_word.upper()  # Ensure the input is in uppercase
    letters = ''.join(letters)  # Join letters into a string
    
    # Check if the word contains only the given letters and does not exceed their counts
    for char in input_word:
        if input_word.count(char) > letters.count(char):
            return "Didn't use required letters."
    
    # Check if the word is valid using the WordsAPI
    if is_valid_word(input_word):
        return "Correct! +1"
    else:
        return "Not a real word."

# Main method to run the word game
def run_read_game(screen, width):
    score = 0
    font_large = pygame.font.SysFont(None, 60)
    font_small = pygame.font.SysFont(None, 40)

    letters = generate_letters()

    running_game = True
    while running_game:
        screen.fill((255, 255, 255))

        # Draw the letters on the screen
        letter_text = font_large.render(f"Given letters: {' '.join(letters)}", True, (0, 0, 0))
        screen.blit(letter_text, (width // 2 - letter_text.get_width() // 2, 150))

        # Display the score
        score_text = font_small.render(f"Score: {score}", True, (0, 128, 0))
        screen.blit(score_text, (20, 20))

        # Event handling for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if the user clicked anywhere (you can add a button if needed)
                # Simple input method: user types word in a text box or enters using the keyboard

        # Handle input from the user (for simplicity using keyboard input)
        user_input = pygame.key.get_pressed()
        # You could add an on-screen input box here or use simple input from the console

        # Example logic for word checking and scoring (change with actual input logic)
        result = check_word('example', letters)  # Replace 'example' with actual input logic
        if result == "Correct! +1":
            score += 1

        result_text = font_small.render(result, True, (0, 0, 0))
        screen.blit(result_text, (width // 2 - result_text.get_width() // 2, 220))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Initialize Pygame and run the game
if __name__ == "__main__":
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Word Game")
    
    run_word_game(screen, width, height)
    pygame.quit()
