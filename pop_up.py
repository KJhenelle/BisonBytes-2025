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


# Button class
class Button:
    def __init__(self, text, x, y, width, height, choice):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.choice = choice  # Store choice letter (A, B, C, D)

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.rect, border_radius=10)
        text_surface = pygame.font.Font(None, 36).render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


# Show a random event and check for correct answer
def show_random_event(screen):
    event = random.choice(events)
    question_text = event["question"]
    choices = event["choices"]
    correct_choice = event["correct"]

    # Display question and choices
    screen.fill((255, 255, 255))  # Clear screen

    question_surface = pygame.font.Font(None, 28).render(question_text, True, (0, 0, 0))
    screen.blit(question_surface, (50, 50))

    buttons = []
    choice_letters = ["A", "B", "C", "D"]
    for i, choice in enumerate(choices):
        button = Button(choice, 50, 150 + i * 60, 700, 50, choice_letters[i])
        buttons.append(button)
        button.draw(screen)

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
                        check_answer(screen, button.choice, correct_choice)  # Check correctness
                        return


# Check if the selected choice is correct
def check_answer(screen, selected_choice, correct_choice):
    screen.fill((255, 255, 255))  # Clear screen

    if selected_choice == correct_choice:
        result_text = "Correct! You handled it well!"
        color = (0, 200, 0)
    else:
        result_text = f"Wrong! Correct answer was {correct_choice}."
        color = (200, 0, 0)

    result_surface = pygame.font.Font(None, 36).render(result_text, True, color)
    screen.blit(result_surface, (50, 300))
    pygame.display.flip()

    time.sleep(2)  # Pause for 2 seconds before returning
    return
