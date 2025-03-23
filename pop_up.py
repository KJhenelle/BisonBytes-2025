import pygame
import random
import time


# List of scenarios with choices and correct answers
events = [
    {
        "question": "The principal walks in unexpectedly. What do you do?",
        "choices": [
            "A. Continue the lesson calmly as if nothing happened.",
            "B. Panic and tell students to behave immediately.",
            "C. Stop teaching and ask the principal what she needs.",
            "D. Whisper to the class stating to be on their best behavior."
        ],
        "correct": "A"
    },
    {
        "question": "A new student joins your class. What is the best approach?",
        "choices": [
            "A. Let student quietly observe and settle in.",
            "B. Ask them to introduce themselves immediately.",
            "C. Give them a tour of the classroom.",
            "D. Introduce them yourself and assign a buddy to help."
        ],
        "correct": "D"
    },
    {
        "question": "Two students start fighting during class. What is your move?",
        "choices": [
            "A. Yell at them to both stop immediately.",
            "B. Separate them and address them calmly.",
            "C. Send both to the principal's office.",
            "D. Ignore it and hope they stop."
        ],
        "correct": "B"
    },
    {
        "question": "A student shows signs of chickenpox. What is your immediate action?",
        "choices": [
            "A. Send student to the nurse immediately.",
            "B. Tell student to wait till lunch.",
            "C. Announce to class that there is an outbreak.",
            "D. Give them a tissue and tell them to wait patiently."
        ],
        "correct": "A"
    },
    {
        "question": "You get a reminder about a parent-teacher conference. What do you do?",
        "choices": [
            "A. Reschedule and send a polite apology.",
            "B. Wing it and hope for the best.",
            "C. Ask another teacher to cover it.",
            "D. Gaslight them and pretend it was not scheduled."
        ],
        "correct": "A"
    },
    {
        "question": "Tech failure during a lesson. What is your next step?",
        "choices": [
            "A. Continue the lesson without the tech.",
            "B. Spend 10 minutes trying to fix it.",
            "C. Let the class take a break while you find a solution.",
            "D. Call it and cancel the lesson."
        ],
        "correct": "A"
    }
]

class Button:
    def __init__(self, text, x, y, width, height, choice):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.choice = choice

    def draw(self, screen, button_color, border_color, text_color):
        pygame.draw.rect(screen, button_color, self.rect, border_radius=5)
        pygame.draw.rect(screen, border_color, self.rect, 2)
        text_surface = pygame.font.Font(None, 18).render(self.text, True, text_color)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# Show a random event and check for correct answer
def show_random_event(screen):
    event = random.choice(events)
    question_text = event["question"]
    choices = event["choices"]
    correct_choice = event["correct"]

    # Colors for pixel art vibe
    background_color = (240, 240, 215)  # Light tan background
    button_color = (255, 223, 186)  # Warm peach button
    border_color = (0, 0, 0)  # Black border for buttons
    text_color = (50, 50, 50)  # Dark gray text
    result_color_correct = (0, 200, 0)  # Green for correct
    result_color_incorrect = (200, 0, 0)  # Red for incorrect

    # Draw background and keep main game visible
    screen.fill(background_color)

    # Pop-up dimensions
    popup_width = 600
    popup_height = 400
    popup_x = (800 - popup_width) // 2
    popup_y = (600 - popup_height) // 2

    # Draw pop-up background with border
    pygame.draw.rect(screen, (0, 0, 0), (popup_x - 5, popup_y - 5, popup_width + 10, popup_height + 10))  # Border
    pygame.draw.rect(screen, background_color, (popup_x, popup_y, popup_width, popup_height))  # Pop-up background

    # Draw question at the top, centered
    question_surface = pygame.font.Font(None, 20).render(question_text, True, text_color)
    question_rect = question_surface.get_rect(center=(popup_x + popup_width // 2, popup_y + 40))
    screen.blit(question_surface, question_rect)

    # Create buttons with pixel art vibe
    buttons = []
    choice_letters = ["A", "B", "C", "D"]
    for i, choice in enumerate(choices):
        button_rect = pygame.Rect(popup_x + 50, popup_y + 100 + i * 60, popup_width - 100, 40)
        button = Button(choice, button_rect.x, button_rect.y, button_rect.width, button_rect.height, choice_letters[i])
        buttons.append(button)
        button.draw(screen, button_color, border_color, text_color)

    pygame.display.flip()

    # Wait until a choice is made
    choice_made = False
    while not choice_made:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_clicked(mouse_pos):
                        choice_made = True
                        if button.choice == correct_choice:
                            result_text = "Correct! You handled it well."
                            result_color = result_color_correct
                        else:
                            result_text = f"Wrong! Correct answer was {correct_choice}."
                            result_color = result_color_incorrect

                        # Show result at the bottom of the pop-up
                        result_surface = pygame.font.Font(None, 20).render(result_text, True, result_color)
                        screen.blit(result_surface, (popup_x + 50, popup_y + popup_height - 40))
                        pygame.display.flip()

                        time.sleep(2)  # Pause for 2 seconds before returning
                        return
