import pygame
import time
import sys

# Import levels
import level1
import level2
import level3

pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer with Multiple Levels")

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GREEN = (50, 255, 100)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
ORANGE = (255, 165, 0)
# Fonts
fontObj = pygame.font.Font('fonts/pixelfont.ttf', 16)

# Sounds
jump_sound = pygame.mixer.Sound("audio/jump.wav")
death_sound = pygame.mixer.Sound("audio/death.wav")
powerup_sound = pygame.mixer.Sound("audio/powerup.wav")
goal_sound = pygame.mixer.Sound("audio/goal.wav")

# Player settings
PLAYER_WIDTH, PLAYER_HEIGHT = 25, 25
player_x, player_y = 375, 500
player_speed = 5
player_dx, player_dy = 0, 0
gravity = 0.6
jump_strength = -12
on_ground = False

# Power-up settings
POWERUP_WIDTH, POWERUP_HEIGHT = 20, 20
powerup_collected_time = None
powerup_active = True
can_double_jump = False

# Levels and game state
levels = [level1, level2, level3]
current_level_index = 0
gate = None
platforms = []
spawn_point = (0, 0)
powerups = []
text_objects = []
death_zones = []


def load_current_level():
    global platforms, powerups, powerup_active, gate, spawn_point, text_objects, death_zones
    platforms, powerups, gate, spawn_point, text_objects, death_zones = levels[current_level_index].load_level()
    powerup_active = len(powerups) > 0


# Main game loop
def main():
    global player_x, player_y, player_dx, player_dy, on_ground, powerup_active, can_double_jump
    global current_level_index, gate, spawn_point, text_objects, powerup_collected_time

    load_current_level()
    player_x, player_y = spawn_point
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Assign Movement to Keys
        keys = pygame.key.get_pressed()
        player_dx = 0
        if keys[pygame.K_LEFT]:
            player_dx = -player_speed
        if keys[pygame.K_RIGHT]:
            player_dx = player_speed
        if keys[pygame.K_SPACE]:
            if on_ground:
                can_double_jump = False
                player_dy = jump_strength
                on_ground = False
                jump_sound.play()
            elif can_double_jump:  # Allow a second jump if power-up is active
                player_dy = jump_strength
                can_double_jump = False  # Reset double jump after using it
                powerup_sound.play()

        # Apply gravity to the player
        player_dy += gravity

        # Update player position
        player_x += player_dx
        player_y += player_dy

        # Create Player Rectangle
        player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

        #Platform Collisions
        on_ground = False
        for platform in platforms:
            if player_rect.colliderect(platform):
                if player_rect.bottom < platform.bottom:
                    player_y = platform.top - PLAYER_HEIGHT
                    player_dy = 0
                    on_ground = True
                elif player_dy < 0 and player_rect.top >= platform.top:
                    player_y = platform.bottom
                    player_dy = 0
                elif player_rect.left >= platform.left:
                    player_x = platform.left - PLAYER_WIDTH
                    player_dx = 0
                elif player_dx < 0 and player_rect.left < platform.right and player_rect.right > platform.right:
                    player_x = platform.right

        # Check collision with power-up
        if powerup_active and powerups:
            powerup_rect = pygame.Rect(powerups[0][0], powerups[0][1], POWERUP_WIDTH, POWERUP_HEIGHT)
            if player_rect.colliderect(powerup_rect):
                powerup_active = False  # Disable power-up after collection
                can_double_jump = True  # Enable double jump ability
                powerup_collected_time = time.time()  # Record the time of collection

        # Reactivate power-up after 5 seconds
        if not powerup_active and powerup_collected_time:
            if time.time() - powerup_collected_time >= 5:
                powerup_active = True
                powerup_collected_time = None  # Reset the timer

        # Check collision with death zones
        for death_zone in death_zones:
            if player_rect.colliderect(death_zone):
                death_sound.play()
                player_x, player_y = spawn_point  # Reset to spawn point
                player_dx, player_dy = 0, 0  # Reset movement
                can_double_jump = False  # Reset double jump
                powerup_active = True
                powerup_collected_time = None

        # Check collision with the level gate
        if gate and player_rect.colliderect(gate):
            goal_sound.play()
            current_level_index += 1
            if current_level_index < len(levels):
                load_current_level()
                player_x, player_y = spawn_point  # Reset player position to new level's spawn point
            else:
                print("You win!")
                pygame.quit()
                sys.exit()

        # Prevent player from going out of bounds
        if player_x < 0:
            player_x = 0
        if player_x + PLAYER_WIDTH > SCREEN_WIDTH:
            player_x = SCREEN_WIDTH - PLAYER_WIDTH
        if player_y + PLAYER_HEIGHT > SCREEN_HEIGHT:
            player_y = SCREEN_HEIGHT - PLAYER_HEIGHT
            on_ground = True
            player_dy = 0
            can_double_jump = False  # Reset double jump when hitting the ground

        # Draw everything
        screen.fill(WHITE)
        for text_obj in text_objects:
            text_surface = fontObj.render(text_obj["content"], True, BLACK)
            screen.blit(text_surface, text_obj["position"])
        pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
        for platform in platforms:
            pygame.draw.rect(screen, GREEN, platform)
        if powerup_active and powerups:
            pygame.draw.rect(screen, ORANGE, (powerups[0][0], powerups[0][1], POWERUP_WIDTH, POWERUP_HEIGHT))
        for death_zone in death_zones:
            pygame.draw.rect(screen, RED, death_zone)
        if gate:
            pygame.draw.rect(screen, YELLOW, gate)
        pygame.display.flip()
        clock.tick(FPS)

 

# Run the game
if __name__ == "__main__":
    main()
