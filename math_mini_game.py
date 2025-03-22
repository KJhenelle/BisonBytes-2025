import pygame
import random
import sys
import time

def run_math_game(screen, width, height):
    import random, time, sys
    score = 0
    correct_streak = 0
    wrong_streak = 0
    game_lost = False
    start_time = time.time()

    font_large = pygame.font.SysFont(None, 60)
    font_small = pygame.font.SysFont(None, 40)

    def generate_question():
        ops = ['+', '-', '*']
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(ops)
        question = f"{a} {op} {b}"
        answer = eval(question)
        return question, answer

    def create_choices(correct):
        choices = [correct]
        while len(choices) < 3:
            fake = correct + random.randint(-10, 10)
            if fake != correct and fake not in choices:
                choices.append(fake)
        random.shuffle(choices)
        return choices

    def flash_game_over():
        for i in range(6):
            screen.fill((255, 0, 0) if i % 2 == 0 else (255, 255, 255))
            text = font_large.render("GAME OVER! 3 wrong in a row!", True, (0, 0, 0))
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2))
            pygame.display.flip()
            pygame.time.wait(400)

    def show_celebration(score):
        for _ in range(60):
            screen.fill((255, 255, 255))
            for _ in range(100):
                x = random.randint(0, width)
                y = random.randint(0, height)
                color = random.choice([(255, 0, 0), (0, 255, 0), (0, 128, 255), (255, 255, 0)])
                pygame.draw.circle(screen, color, (x, y), 5)
            text = font_large.render(f"Time's up! Final Score: {score}", True, (0, 0, 0))
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2))
            pygame.display.flip()
            pygame.time.Clock().tick(30)

    question, answer = generate_question()
    choices = create_choices(answer)

    button_rects = [
        pygame.Rect(300, 300, 200, 60),
        pygame.Rect(300, 380, 200, 60),
        pygame.Rect(300, 460, 200, 60),
    ]

    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((255, 255, 255))
        time_left = max(0, 30 - int(time.time() - start_time))

        if time_left <= 0:
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for idx, rect in enumerate(button_rects):
                    if rect.collidepoint(mouse_pos):
                        if choices[idx] == answer:
                            correct_streak += 1
                            wrong_streak = 0
                            if correct_streak == 3:
                                score += 1
                                correct_streak = 0
                        else:
                            wrong_streak += 1
                            correct_streak = 0
                            if wrong_streak == 3:
                                game_lost = True
                                running = False
                                break  # 🚨 Exit IMMEDIATELY after 3rd wrong

                        if not game_lost:
                            question, answer = generate_question()
                            choices = create_choices(answer)

        if game_lost:
            break

        # Draw question
        q_surface = font_large.render(question, True, (0, 0, 0))
        screen.blit(q_surface, (width // 2 - q_surface.get_width() // 2, 150))

        # Draw answer buttons
        for i, rect in enumerate(button_rects):
            pygame.draw.rect(screen, (173, 216, 230), rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)
            choice_text = font_small.render(str(choices[i]), True, (0, 0, 0))
            screen.blit(choice_text, (rect.x + 75, rect.y + 15))

        # HUD
        score_text = font_small.render(f"Score: {score}", True, (0, 128, 0))
        timer_text = font_small.render(f"Time Left: {time_left}s", True, (255, 0, 0))
        correct_text = font_small.render(f"Streak: {correct_streak}/3", True, (0, 0, 255))
        wrong_text = font_small.render(f"Mistakes: {wrong_streak}/3", True, (255, 0, 0))

        screen.blit(score_text, (20, 20))
        screen.blit(timer_text, (600, 20))
        screen.blit(correct_text, (20, 60))
        screen.blit(wrong_text, (20, 100))

        pygame.display.flip()
        clock.tick(60)

    # Final screen
    if game_lost:
        flash_game_over()
    else:
        show_celebration(score)

    pygame.time.wait(1000)
