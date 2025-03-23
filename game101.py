import pygame
import sys
import random
from scenario import popscene1
from math_mini_game import run_math_game
from read_mini_game import run_read_game
from pop_up import show_random_event

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Classroom Game")

# Load and scale background
background = pygame.transform.scale(pygame.image.load("assets/background/classroom_chaos_main_background.png").convert(), (width, height))

# Progress bar setup
progress_bar = pygame.transform.scale(pygame.image.load("assets/background/progress_bar.png").convert_alpha(), (600, 30))
progress_sprite = pygame.transform.scale(pygame.image.load("assets/background/progress_sprite.png").convert_alpha(), (30, 40))
end_sprite = pygame.transform.scale(pygame.image.load("assets/background/end_sprite.png").convert_alpha(), (40, 50))
progress = 0
max_progress = 100

# Table definitions (same as before)
# [Previous table definitions remain unchanged...]

# Modified table states initialization
table_states = []
for table in student_tables:
    table_states.append({
        "rect": table, "clickable": False, "timer": 0, 
        "sprite_index": 4, "cooldown": random.randint(15, 45),
        "addressed": False, "health_decreased": False, "is_task": False
    })
for table in task_tables:
    table_states.append({
        "rect": table, "clickable": True, "timer": 0,
        "sprite_index": 0, "cooldown": 0, 
        "addressed": False, "health_decreased": False, "is_task": True
    })

# Timer sprites and health images (same as before)
# [Previous asset loading remains unchanged...]

def draw_progress_bar():
    screen.blit(progress_bar, (100, height-50))
    screen.blit(end_sprite, (100 + 600 - 40, height-60))
    x_pos = 100 + (progress / max_progress) * (600 - 40)
    screen.blit(progress_sprite, (x_pos, height-60))

# Modified show_scenario_screen to handle health gain
def show_scenario_screen(scenario, options, table_number):
    global health, progress
    # [Previous scenario display code remains unchanged...]
    
    # After user selects an option:
    # Assume correct answer adds progress (modify based on your game logic)
    progress += 10  # Example: 10% per correct answer
    if progress >= max_progress:
        progress = max_progress

# Modified go_to_next_screen
def go_to_next_screen(table_number):
    global progress
    # [Previous code remains unchanged...]
    # Add progress for addressing tables
    if table_number != 10:  # Example: Only student tables add progress
        progress += 5
        if progress >= max_progress:
            progress = max_progress

# Modified main game loop
running = True
clock = pygame.time.Clock()
event_timer = random.randint(10, 20)
game_outcome = None  # None = playing, "win" or "lose"

while running:
    dt = clock.tick(60) / 1000

    # Event handling (same as before)
    # [Previous event handling remains unchanged...]

    # Handle random events with health gain
    event_timer -= dt
    if event_timer <= 0:
        if show_random_event(screen):  # Assume returns True if answered correctly
            health = min(5, health + 1)
        event_timer = random.randint(15, 30)

    # Update table states (modified for task tables)
    for state in table_states:
        if state["is_task"]:
            continue  # Skip updates for task tables
            
        if state["cooldown"] > 0:
            state["cooldown"] -= dt
            if state["cooldown"] <= 0:
                # Cooldown logic for student tables
                state["cooldown"] = 0
                state["clickable"] = True
                state["sprite_index"] = 0
                state["addressed"] = False
                state["health_decreased"] = False
        elif state["clickable"]:
            state["timer"] += dt
            if state["timer"] >= 5:
                state["timer"] = 0
                state["sprite_index"] += 1
                if state["sprite_index"] >= 4:
                    state["clickable"] = False
                    state["cooldown"] = 10
                    if not state["addressed"] and not state["health_decreased"]:
                        health -= 1
                        state["health_decreased"] = True

    # Check win/lose conditions
    if health <= 0:
        game_outcome = "lose"
        running = False
    elif progress >= max_progress:
        game_outcome = "win"
        running = False

    # Drawing
    screen.blit(background, (0, 0))
    
    # Draw tables
    for state in table_states:
        if state["is_task"]:
            screen.blit(timer_sprites[0], state["rect"].topleft)
        elif state["clickable"] and state["sprite_index"] < 4:
            screen.blit(timer_sprites[state["sprite_index"]], state["rect"].topleft)
        elif state["sprite_index"] == 4:
            screen.blit(timer_sprites[4], state["rect"].topleft)

    # Draw health and progress
    screen.blit(health_images[min(5, health)], (10, 10))
    draw_progress_bar()
    pygame.display.flip()

# Handle game end
if game_outcome == "win":
    # Display win screen
    pass
elif game_outcome == "lose":
    # Display lose screen
    pass

pygame.quit()
sys.exit()