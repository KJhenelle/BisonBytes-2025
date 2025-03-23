import pygame
import random
import sys
import time
import os

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
    background = pygame.image.load("assets/background/chalkboard.png")
    background = background.convert()
    background = pygame.transform.scale(background, (width, height))

    score = 0
    start_time = time.time()
    font_large = pygame.font.SysFont(None, 60)
    font_small = pygame.font.SysFont(None, 40)

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

    button_rects = [
        pygame.Rect(300, 300, 200, 60),
        pygame.Rect(300, 380, 200, 60),
        pygame.Rect(300, 460, 200, 60),
    ]

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
                        question, answer = generate_question()
                        choices = create_choices(answer)

        q_surface = font_large.render(question, True, (0, 0, 0))
        screen.blit(q_surface, (width // 2 - q_surface.get_width() // 2, 150))

        for i, rect in enumerate(button_rects):
            pygame.draw.rect(screen, (173, 216, 230), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)
            choice_text = font_small.render(str(choices[i]), True, (0, 0, 0))
            screen.blit(choice_text, (rect.x + 75, rect.y + 15))

        timer = 30 - int(time.time() - start_time)
        score_text = font_small.render(f"Score: {score}", True, (0, 128, 0))
        timer_text = font_small.render(f"Time Left: {timer}s", True, (255, 0, 0))
        screen.blit(score_text, (20, 20))
        screen.blit(timer_text, (600, 20))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    screen.fill((255, 255, 255))
    final_text = font_large.render(f"Time's up! Score: {score}", True, (0, 0, 0))
    screen.blit(final_text, (width // 2 - final_text.get_width() // 2, height // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
