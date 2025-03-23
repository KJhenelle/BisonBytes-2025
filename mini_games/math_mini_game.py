import pygame
import random
import sys
import time

def generate_question():
    ops = ['+', '-', '*']
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(ops)

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:
        result = a * b

    question = f"{a} {op} {b}"
    return question, result

def run_math_game(screen, width, height):
    score = 0
    start_time = time.time()

    font_large = pygame.font.SysFont(None, 60)
    font_small = pygame.font.SysFont(None, 40)

    background = pygame.image.load("assets/background/chalkboard.png").convert()
    background = pygame.transform.scale(background, (width, height))

    def create_choices(correct):
        choices = [correct]
        while len(choices) < 3:
            fake = correct + random.randint(-10, 10)
            if fake != correct and fake not in choices:
                choices.append(fake)
        random.shuffle(choices)
        return choices

    question, answer = generate_question()
    choices = create_choices(answer)

    button_y_start = 230
    button_spacing = 80
    button_rects = [
        pygame.Rect(width // 2 - 100, button_y_start + i * button_spacing, 200, 60)
        for i in range(3)
    ]

    classroom_button = pygame.Rect(20, height - 80, 200, 50)

    running_game = True
    while running_game and time.time() - start_time < 30:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for idx, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        if choices[idx] == answer:
                            score += 1
                            if score >= 5:
                                running_game = False
                                break  # Stop checking other buttons
                        if running_game:  # Only update if still playing
                            question, answer = generate_question()
                            choices = create_choices(answer)

                if classroom_button.collidepoint(mouse_pos):
                    running_game = False
                    break

        q_surface = font_large.render(question, True, (255, 255, 255))
        screen.blit(q_surface, (width // 2 - q_surface.get_width() // 2, 150))

        for i, rect in enumerate(button_rects):
            pygame.draw.rect(screen, (255, 255, 204), rect, border_radius=10)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2, border_radius=10)

            choice_text = font_small.render(str(choices[i]), True, (0, 0, 0))
            screen.blit(choice_text, (rect.x + 75, rect.y + 15))

        pygame.draw.rect(screen, (200, 200, 255), classroom_button, border_radius=10)
        pygame.draw.rect(screen, (0, 0, 100), classroom_button, 2, border_radius=10)
        class_text = font_small.render("Back", True, (0, 0, 100))
        screen.blit(class_text, (classroom_button.x + 10, classroom_button.y + 10))

        timer = 30 - int(time.time() - start_time)
        score_text = font_small.render(f"Score: {score}", True, (0, 128, 0))
        timer_text = font_small.render(f"Time Left: {timer}s", True, (255, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(timer_text, (600, 20))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # Show final screen
    screen.blit(background, (0, 0))
    if score >= 5:
        final_msg = "Great job! You got 5 correct answers!"
    elif time.time() - start_time >= 30:
        final_msg = f"Time's up! Score: {score}"
    else:
        return  # Early return to main menu via classroom button
    
    final_text = font_large.render(final_msg, True, (255, 255, 255))
    screen.blit(final_text, (width // 2 - final_text.get_width() // 2, height // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

    return  # So it can return back to the main menu
