import pygame

def load_level():
    platforms = [
        pygame.Rect(100, 500, 150, 20),
        pygame.Rect(300, 400, 150, 20),
        pygame.Rect(500, 300, 150, 20),
        pygame.Rect(100, 100, 150, 20),
    ]
    spawn_point = (100, 475)
    powerups = [(360, 200)]
    gate = pygame.Rect(160, 50, 30, 50)
    death_zones = [
        pygame.Rect(300, 480, 20, 20),  # Add a spike at (300, 480)
        pygame.Rect(600, 380, 20, 20),  # Add another spike
    ]
    text_objects = [
        {"content": "Welcome to Level 1!", "position": (10, 10)}
    ]
    return platforms, powerups, gate, spawn_point, text_objects, death_zones