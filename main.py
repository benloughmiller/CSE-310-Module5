import pygame
import sys

# Import levels
import level1
import level2

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

#Sounds
jump_sound = pygame.mixer.Sound("audio/jump.wav")

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
powerup_active = True
can_double_jump = False

# Levels and game state
levels = [level1, level2]
current_level_index = 0
gate = None  # Initialize the gate for the level
spawn_point = (375, 500)  # Default spawn point

def load_current_level():
    global platforms, powerups, powerup_active, gate, spawn_point
    platforms, powerups, gate, spawn_point = levels[current_level_index].load_level()
    powerup_active = len(powerups) > 0

# Main game loop
def main():
    global player_x, player_y, player_dx, player_dy, on_ground, powerup_active, can_double_jump, current_level_index, gate, spawn_point

    load_current_level()

    # Set player spawn location based on the level
    player_x, player_y = spawn_point  # Reset player to spawn point

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
                player_dy = jump_strength
                on_ground = False
                jump_sound.play()
            elif can_double_jump:  # Allow a second jump if power-up is active
                player_dy = jump_strength
                can_double_jump = False  # Reset double jump after using it
                jump_sound.play()

        # Apply gravity to the player
        player_dy += gravity

        # Update player position
        player_x += player_dx
        player_y += player_dy

        # Create Player Rectangle
        player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)

        # Check collisions with platforms
        on_ground = False
        for platform in platforms:
            if player_rect.colliderect(platform):
                # Platform Top Collision
                if player_dy > 0 and player_rect.bottom <= platform.bottom:
                    player_y = platform.top - PLAYER_HEIGHT
                    player_dy = 0
                    on_ground = True
                # Platform Underside Collision
                elif player_dy < 0 and player_rect.top >= platform.top:
                    player_y = platform.bottom
                    player_dy = 0

        # Check collision with power-up
        if powerup_active and powerups:
            powerup_rect = pygame.Rect(powerups[0][0], powerups[0][1], POWERUP_WIDTH, POWERUP_HEIGHT)
            if player_rect.colliderect(powerup_rect):
                powerup_active = False  # Disable power-up after collection
                can_double_jump = True  # Enable double jump ability

        # Check collision with the level gate
        if gate and player_rect.colliderect(gate):
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
        # Draw Player
        pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))
        # Draw Platforms
        for platform in platforms:
            pygame.draw.rect(screen, GREEN, platform)
        # Draw Power-ups
        if powerup_active and powerups:
            pygame.draw.rect(screen, RED, (powerups[0][0], powerups[0][1], POWERUP_WIDTH, POWERUP_HEIGHT))
        # Draw Gate
        if gate:
            pygame.draw.rect(screen, YELLOW, gate)
        pygame.display.flip()
        clock.tick(FPS)

# Run the game
if __name__ == "__main__":
    main()
