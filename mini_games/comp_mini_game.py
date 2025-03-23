import pygame
import random
import time
import json

def run_typing_game(screen, width, height):
    # Load game assets and initialize variables
    
    background_image = pygame.image.load("assets/background/computer_screen.png").convert()
    background_image = pygame.transform.scale(background_image, (width, height))
    
    colors = {
        "BAR": (25, 32, 55),
        "FRAME": (135, 141, 153),
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "GREEN": (0, 255, 0)
    }
    
    font = pygame.font.Font(None, 36)
    input_font = pygame.font.Font(None, 48)
    
    # Game state
    game_vars = {
        "words": ["apple", "banana", "cherry", "date", "elephant", "giraffe", 
                 "honey", "ice", "jaguar", "kite", "lemon", "monkey"],
        "word_speed": 1,
        "input_text": '',
        "score": 0,
        "current_word": None,
        "word_y": 0,
        "spacing": 80,
        "start_time": time.time(),
        "running": True
    }
    
    instructions = "Type the falling words to score points! Press Enter to submit. Need a 70 to Pass!"
    
    # Helper functions
    def wrap_text(text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = words[0]
        for word in words[1:]:
            if font.size(current_line + ' ' + word)[0] <= max_width:
                current_line += ' ' + word
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        return lines
    
    def draw_button():
        btn_text = font.render("Check on Class", True, colors["BAR"])
        btn_rect = btn_text.get_rect()
        btn_rect.topleft = (10, height - 50)
        pygame.draw.rect(screen, colors["WHITE"], btn_rect.inflate(20, 10))
        screen.blit(btn_text, btn_rect)
        return btn_rect.inflate(20, 10)
    
    def save_score():
        data = {"score": game_vars["score"]}
        with open("jsons/comp_mini_game_data.json", "w") as f:
            json.dump(data, f)

    # Main game loop
    instruction_lines = wrap_text(instructions, font, width-20)
    instruction_height = len(instruction_lines) * 40 + 20
    
    while game_vars["running"]:
        screen.blit(background_image, (0, 0))
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_vars["running"] = False
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    game_vars["input_text"] = game_vars["input_text"][:-1]
                elif event.key == pygame.K_RETURN:
                    if game_vars["current_word"] and game_vars["input_text"] == game_vars["current_word"][0]:
                        game_vars["score"] += 10
                        game_vars["current_word"] = None
                    game_vars["input_text"] = ''
                else:
                    game_vars["input_text"] += event.unicode
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    save_score()
                    game_vars["running"] = False

        # Game logic
        if not game_vars["current_word"]:
            game_vars["current_word"] = [
                random.choice(game_vars["words"]),
                instruction_height
            ]
            
        if game_vars["current_word"]:
            word, y_pos = game_vars["current_word"]
            text_surf = font.render(word, True, colors["BLACK"])
            screen.blit(text_surf, (width//2 - text_surf.get_width()//2, y_pos))
            game_vars["current_word"][1] += game_vars["word_speed"]
            
            if y_pos >= height:
                game_vars["current_word"] = None

        # UI drawing
        pygame.draw.rect(screen, colors["FRAME"], (0, 0, width, instruction_height))
        for i, line in enumerate(instruction_lines):
            text = font.render(line, True, colors["WHITE"])
            screen.blit(text, (10, 10 + i*40))
            
        button_rect = draw_button()
        
        # Input area
        pygame.draw.line(screen, colors["BLACK"], (0, height-5), (width, height-5), 2)
        pygame.draw.rect(screen, colors["BAR"], (0, height-5, width, 60))
        
        input_surf = input_font.render(game_vars["input_text"], True, colors["WHITE"])
        screen.blit(input_surf, (width//2 - input_surf.get_width()//2, height-50))
        
        # Score display
        score_text = font.render(f"Grade: {game_vars['score']}", True, colors["WHITE"])
        screen.blit(score_text, (10, instruction_height + 10))
        
        if game_vars["score"] >= 70:
            pass_text = font.render("You Passed!", True, colors["GREEN"])
            screen.blit(pass_text, (width//2 - pass_text.get_width()//2, height//2))

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    # Cleanup and return to main
    save_score()
    return