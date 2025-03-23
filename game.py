# import pygame
# import sys
# import random
# from scenario import popscene1
# from math_mini_game import run_math_game
# from read_mini_game import run_read_game
# from pop_up import show_random_event

# # Initialize Pygame
# pygame.init()

# # Set up the display
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Classroom Game")

# # Load the background image
# background = pygame.image.load("assets/background/classroom_chaos_main_background.png")
# background = background.convert()
# background = pygame.transform.scale(background, (width, height))

# # Progress bar assets
# progress_bar = pygame.transform.scale(pygame.image.load("assets/background/progress_bar.png").convert_alpha(), (600, 30))
# progress_sprite = pygame.transform.scale(pygame.image.load("assets/background/progress_sprite.png").convert_alpha(), (30, 40))
# end_sprite = pygame.transform.scale(pygame.image.load("assets/background/progress_sprite.png").convert_alpha(), (40, 50))
# progress = 0
# max_progress = 100

# # Define clickable areas (tables)
# student_tables = [
#     pygame.Rect(100, 250, 125, 100), pygame.Rect(265, 250, 125, 100),
#     pygame.Rect(420, 250, 125, 100), pygame.Rect(580, 250, 125, 100),
#     pygame.Rect(100, 370, 125, 100), pygame.Rect(265, 370, 125, 100),
#     pygame.Rect(420, 370, 125, 100), pygame.Rect(580, 370, 125, 100)
# ]

# task_tables = [
#     pygame.Rect(95, 470, 125, 100), pygame.Rect(260, 470, 125, 100),
#     pygame.Rect(425, 470, 125, 100), pygame.Rect(305, 120, 200, 125),
#     pygame.Rect(515, 100, 80, 100)
# ]

# # Table states
# table_states = []
# for table in student_tables:
#     table_states.append({
#         "rect": table, "clickable": False, "timer": 0,
#         "sprite_index": 4, "cooldown": random.randint(15, 45),
#         "addressed": False, "health_decreased": False, "is_task": False
#     })
    
# for table in task_tables:
#     table_states.append({
#         "rect": table, "clickable": True, "timer": 0,
#         "sprite_index": 0, "cooldown": 0,
#         "addressed": False, "health_decreased": False, "is_task": True
#     })

# # Load sprites
# timer_sprites = [pygame.image.load(f"assets/background/sprite_{i}.png").convert_alpha() for i in range(5)]
# health_images = {
#     5: pygame.image.load("assets/background/5.png").convert_alpha(),
#     4: pygame.image.load("assets/background/4-3.png").convert_alpha(),
#     3: pygame.image.load("assets/background/4-3.png").convert_alpha(),
#     2: pygame.image.load("assets/background/2.png").convert_alpha(),
#     1: pygame.image.load("assets/background/1.png").convert_alpha()
# }
# health = 5

# def wrap_text(text, font, max_width):
#     words = text.split(" ")
#     lines = []
#     current_line = ""
#     for word in words:
#         test_line = f"{current_line} {word}" if current_line else word
#         if font.size(test_line)[0] <= max_width:
#             current_line = test_line
#         else:
#             lines.append(current_line)
#             current_line = word
#     if current_line:
#         lines.append(current_line)
#     return lines

# def show_scenario_screen(scenario, options, table_number):
#     global health, progress
#     if not scenario:
#         font = pygame.font.Font(None, 36)
#         screen.blit(background, (0, 0))
#         screen.blit(font.render("No scenario available", True, (255, 255, 255)), (50, 50))
#         pygame.display.flip()
#         pygame.time.delay(2000)
#         return

#     screen.fill((255, 255, 255))
#     font = pygame.font.Font(None, 36)
#     y_offset = 50
    
#     for line in wrap_text(scenario, font, width - 100):
#         screen.blit(font.render(line, True, (0, 0, 0)), (50, y_offset))
#         y_offset += 30

#     option_rects = []
#     for i, option in enumerate(options):
#         option_lines = wrap_text(option, font, width - 100)
#         for j, line in enumerate(option_lines):
#             screen.blit(font.render(line, True, (0, 0, 0)), (50, y_offset + j * 30))
#         option_rect = pygame.Rect(50, y_offset, width - 100, len(option_lines) * 30)
#         pygame.draw.rect(screen, (0, 0, 255), option_rect, 2)
#         option_rects.append(option_rect)
#         y_offset += len(option_lines) * 30 + 20

#     pygame.display.flip()
    
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 for i, rect in enumerate(option_rects):
#                     if rect.collidepoint(mouse_pos):
#                         progress += 10
#                         health = min(5, health + 1)
#                         waiting = False
#                         break

# def go_to_next_screen(table_number):
#     global progress
#     if table_number == 10:
#         run_math_game(screen, width, height)
#     else:
#         scenario, options = popscene1(random.randint(1, 8))
#         show_scenario_screen(scenario, options, table_number)
#     progress += 5

# def draw_progress_bar():
#     screen.blit(progress_bar, (100, height-50))
#     screen.blit(end_sprite, (100 + 600 - 40, height-60))
#     x_pos = 100 + (progress / max_progress) * (600 - 40)
#     screen.blit(progress_sprite, (x_pos, height-60))

# # Main game loop
# running = True
# clock = pygame.time.Clock()
# event_timer = random.randint(10, 20)
# game_outcome = None

# while running:
#     dt = clock.tick(60) / 1000

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_pos = pygame.mouse.get_pos()
#             for i, state in enumerate(table_states):
#                 if state["rect"].collidepoint(mouse_pos) and state["clickable"]:
#                     if not state["is_task"]:
#                         state["clickable"] = False
#                         state["timer"] = 0
#                         state["sprite_index"] = 4
#                         state["cooldown"] = random.randint(15, 45)
#                         state["addressed"] = True
#                     go_to_next_screen(i+1)
#                     break

#     # Random events
#     event_timer -= dt
#     if event_timer <= 0:
#         if show_random_event(screen):
#             health = min(5, health + 1)
#             progress += 15
#         event_timer = random.randint(15, 30)

#     # Update student tables
#     for state in table_states:
#         if state["is_task"]:
#             continue
            
#         if state["cooldown"] > 0:
#             state["cooldown"] -= dt
#             if state["cooldown"] <= 0:
#                 state.update({
#                     "cooldown": 0,
#                     "clickable": True,
#                     "sprite_index": 0,
#                     "addressed": False,
#                     "health_decreased": False
#                 })
#         elif state["clickable"]:
#             state["timer"] += dt
#             if state["timer"] >= 5:
#                 state["timer"] = 0
#                 state["sprite_index"] += 1
#                 if state["sprite_index"] >= 4:
#                     state["clickable"] = False
#                     state["cooldown"] = 10
#                     if not state["addressed"] and not state["health_decreased"]:
#                         health -= 1
#                         state["health_decreased"] = True

#     # Check win/lose conditions
#     if health <= 0:
#         game_outcome = "lose"
#         running = False
#     elif progress >= max_progress:
#         game_outcome = "win"
#         running = False

#     # Draw everything
#     screen.blit(background, (0, 0))
    
#     for state in table_states:
#         if state["is_task"]:
#             screen.blit(timer_sprites[0], state["rect"].topleft)
#         elif state["clickable"] and state["sprite_index"] < 4:
#             screen.blit(timer_sprites[state["sprite_index"]], state["rect"].topleft)
#         elif state["sprite_index"] == 4:
#             screen.blit(timer_sprites[4], state["rect"].topleft)

#     screen.blit(health_images[min(5, health)], (10, 10))
#     draw_progress_bar()
#     pygame.display.flip()

# # End screen
# end_font = pygame.font.Font(None, 72)
# screen.fill((0, 0, 0))
# if game_outcome == "win":
#     text = end_font.render("YOU WIN!", True, (0, 255, 0))
# elif game_outcome == "lose":
#     text = end_font.render("GAME OVER", True, (255, 0, 0))
# screen.blit(text, (width//2 - text.get_width()//2, height//2 - text.get_height()//2))
# pygame.display.flip()
# pygame.time.delay(3000)

# pygame.quit()
# sys.exit()