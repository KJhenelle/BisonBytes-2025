import pygame
import random
import requests
import json
import subprocess
import itertools  # Ensure this is imported

# WordsAPI details (sign up for an API key at https://www.wordsapi.com/)
API_KEY = 'eaec32556bmsh376df1c06bc17bap1a5c3ajsn5c63b63563ef'
BASE_URL = 'https://wordsapiv1.p.rapidapi.com/words/'

# Define color variables for easy customization
BEIGE = (229, 202, 172)
CHECK_BUTTON_COLOR = (238,221,195)  # white-tanish
CHECK_BUTTON_TEXT_COLOR = (184, 136, 100)  # brown

REGENERATE_BUTTON_COLOR = (184, 136, 100)  # brown
REGENERATE_BUTTON_TEXT_COLOR = (225, 225, 255) #white

# Function to generate random letters that can form at least one valid word
def generate_letters():
    while True:
        # Generate 4 random letters
        letters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4)
        
        # Check if there is at least one valid word using these letters
        possible_words = generate_possible_words(letters)
        if any(is_valid_word(word) for word in possible_words):
            return letters  # Return the valid set of letters

# Generate possible words using permutations of the 4 letters
def generate_possible_words(letters):
    possible_words = []
    # Generate words of different lengths (2 to 4 letters long)
    for length in range(2, 5):
        possible_words += [''.join(p) for p in itertools.permutations(letters, length)]
    return possible_words

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
def check_word(input_word, letters, correct_words):
    input_word = input_word.upper()  # Ensure the input is in uppercase
    letters = ''.join(letters)  # Join letters into a string
    
    # Check if the word contains only the given letters and does not exceed their counts
    for char in input_word:
        if input_word.count(char) > letters.count(char):
            return "Didn't use required letters."
        
    # Check if the word has already been guessed correctly
    if input_word in correct_words:
        return "You've already guessed that word."
    
    # Check if the word is valid using the WordsAPI
    if is_valid_word(input_word):
        return "Correct! +10"
    else:
        return "Not a real word."

# Function to handle the text input
def handle_input(event, input_text):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            input_text = input_text[:-1]  # Remove last character
        elif event.key != pygame.K_RETURN:  # Avoid adding the "Enter" key
            input_text += event.unicode  # Add character to input text
    return input_text

# Function to create a button (for the 'Regenerate Letters' and 'Check on Classroom' actions)
def create_button(screen, text, font, x, y, padding, button_color, text_color):
    # Calculate the size of the text and add padding
    text_surface = font.render(text, True, text_color)
    button_width = text_surface.get_width() + padding * 2  # Add padding to both sides of the text
    button_height = text_surface.get_height() + padding * 2  # Add padding to top and bottom

    button_rect = pygame.Rect(x, y, button_width, button_height)
    pygame.draw.rect(screen, button_color, button_rect)  # button color
    screen.blit(text_surface, (x + (button_width - text_surface.get_width()) // 2, y + (button_height - text_surface.get_height()) // 2))  # Center the text

    return button_rect

# Function to wrap text into multiple lines based on the screen width
def wrap_text(text, font, screen_width):
    words = text.split(' ')
    lines = []
    current_line = ''
    
    for word in words:
        # Add the word to the current line if it fits
        if font.size(current_line + ' ' + word)[0] <= screen_width - 40:  # Subtract some padding
            current_line += ' ' + word
        else:
            # Otherwise, start a new line
            if current_line:
                lines.append(current_line)
            current_line = word
    
    # Add the last line
    if current_line:
        lines.append(current_line)
    
    return lines

# Function to create a button (for the 'Regenerate Letters' and 'Check on Classroom' actions)
def create_button(screen, text, font, x, y, width, height, button_color, text_color):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, button_color, button_rect)  # button color
    text_surface = font.render(text, True, text_color)  # Use the specified text color
    screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y + (height - text_surface.get_height()) // 2))
    return button_rect

# Function to save the score to a JSON file
def save_score(score):
    data = {"score": score}
    with open("jsons/read_mini_game_data.json", "w") as file:  # Save to read_mini_game_data.json
        json.dump(data, file)

# Main method to run the word game
def run_read_game(screen, width):
    score = 0
    beige = (229,202,172)

    font_large = pygame.font.Font('assets/fonts/Jersey_25/Jersey25-Regular.ttf', 50)
    font_small = pygame.font.Font('assets/fonts/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 30)
    font_instructions = pygame.font.Font('assets/fonts/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 28)  # Font for instructions
    font_check_button = pygame.font.Font('assets/fonts/Pixelify_Sans/PixelifySans-VariableFont_wght.ttf', 28)

    letters = generate_letters()  # Generate letters that can form a word
 
    input_text = ""  # Initialize the input text
    correct_words = []  # List to store correct words
    incorrect_words = []  # List to store incorrect words
    running_game = True

    # Instruction text
    instructions_text = "Use the letters to make words. Press Enter to submit. Click 'Regenerate Letters' to get new ones. Need a 70!"

    # Wrap the instruction text
    wrapped_instructions = wrap_text(instructions_text, font_instructions, width)

    # Adjust the y position for the "Check on Classroom" button to avoid clipping
    check_button_y_position = height - 20  # Place it a bit higher to ensure it doesn't get clipped

    # Adjust the x-position for the "Check on Classroom" button to prevent it from being clipped on the left
    check_button_x_position = 0  # Give it a margin from the left sid

    while running_game:
        screen.fill((255, 255, 255))

        background_image = pygame.image.load('classroom_desk.jpeg')
        background_image = pygame.transform.scale(background_image, (width, height))
        background_rect = background_image.get_rect()  # Get the size of the image for proper positioning
        screen.blit(background_image, background_rect)

        # Display wrapped instructions at the top of the screen
        y_offset = 20
        for line in wrapped_instructions:
            instructions_display = font_instructions.render(line, True, (0, 0, 0))
            screen.blit(instructions_display, (20, y_offset))
            y_offset += font_instructions.get_height()

        # Draw the letters on the screen
        letter_text = font_large.render(f"Given letters: {' '.join(letters)}", True, (0, 0, 0))
        screen.blit(letter_text, (width // 2 - letter_text.get_width() // 2, 150))

        # Display the score
        score_text = font_small.render(f"Grade: {score}", True, (0, 0, 0))
        score_rect = pygame.Rect(20, 100, score_text.get_width() + 20, score_text.get_height() + 10)  # Adjust for padding
        pygame.draw.rect(screen, beige, score_rect)
        screen.blit(score_text, (score_rect.x + 10, score_rect.y + 5))  # Add padding to center the text inside the rectangle


        # Display the input text
        input_text_display = font_small.render(f"Input: {input_text}", True, (0, 0, 0))
        screen.blit(input_text_display, (width // 2 - input_text_display.get_width() // 2, 250))

        # Display correct and incorrect words
            #correct words
        correct_label = font_small.render("Correct Words:", True, (0, 128, 0))
        correct_label_rect = pygame.Rect(50, 350, correct_label.get_width() + 20, correct_label.get_height() + 10)  # Background rectangle for the label
        pygame.draw.rect(screen, beige, correct_label_rect)  # Draw beige background
        screen.blit(correct_label, (correct_label_rect.x + 10, correct_label_rect.y + 5))  # Blit the label text on top with padding

        for i, word in enumerate(correct_words):
            word_text = font_small.render(word, True, (0, 128, 0))
            screen.blit(word_text, (50, 400 + (i * 30)))  
    
            #incorrect words
        incorrect_label = font_small.render("Incorrect Words:", True, (255, 0, 0))
        incorrect_label_rect = pygame.Rect(480, 350, incorrect_label.get_width() + 20, incorrect_label.get_height() + 10)  # Background rectangle for the label
        pygame.draw.rect(screen, beige, incorrect_label_rect)  # Draw beige background
        screen.blit(incorrect_label, (incorrect_label_rect.x + 10, incorrect_label_rect.y + 5))  # Blit the label text on top with padding

        for i, word in enumerate(incorrect_words):
            word_text = font_small.render(word, True, (255, 0, 0))
            screen.blit(word_text, (480, 400 + (i * 30)))

        # Display regenerate button and handle click
        button_width = 300
        x_position = (width - button_width) // 2  
        regenerate_button_rect = create_button(screen, "Regenerate Letters", font_small, x_position, 500, 350, 50, REGENERATE_BUTTON_COLOR, REGENERATE_BUTTON_TEXT_COLOR)
        if regenerate_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            letters = generate_letters()  # Regenerate letters when clicked

        # Display "Check on Classroom" button and handle click
        check_button_rect = create_button(screen, "Check on Classroom", font_check_button, check_button_x_position, check_button_y_position, 300, 20, CHECK_BUTTON_COLOR, CHECK_BUTTON_TEXT_COLOR)  # Adjusted y-position and padding
        if check_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            save_score(score)  # Save score to JSON file
            pygame.quit()  # Close the current game window
            subprocess.run(["python", "game101.py"])  # Run game101.py script to return to that game

        # Event handling for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Handle user input for typing
            if event.type == pygame.KEYDOWN:
                input_text = handle_input(event, input_text)

            # Handle "Enter" key to submit the word
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                result = check_word(input_text, letters, correct_words)
                if result == "Correct! +10":
                    score += 10
                    correct_words.append(input_text.upper())  # Add to correct words
                else:
                    incorrect_words.append(input_text.upper())  # Add to incorrect words
                input_text = ""  # Clear input after submitting

        # Check if the player has passed
        if score >= 70:
            pass_text = font_large.render("You Passed!", True, (0, 255, 0))
            screen.blit(pass_text, (width // 2 - pass_text.get_width() // 2, 300))

        # Update the screen
        pygame.display.flip()
        pygame.time.Clock().tick(60)

# Initialize Pygame and run the game
if __name__ == "__main__":
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Word Game")
    
    run_read_game(screen, width)
    pygame.quit()