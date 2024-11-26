import pygame

def load_level():
    platforms = [
        pygame.Rect(100, 500, 150, 20),
        pygame.Rect(300, 400, 150, 20),
        pygame.Rect(500, 300, 150, 20),
        pygame.Rect(100, 100, 150, 20),
    ]
    spawn_point = (100, 475)
    powerups = [pygame.Rect(360, 200, 20, 20)]
    gate = pygame.Rect(160, 50, 30, 50)
    death_zones = [
        pygame.Rect(0, 580, 800, 20)
    ]
    text_objects = [
        {"content": "This powerup allows you to jump again", "position": (300, 150)}
    ]
    return platforms, powerups, gate, spawn_point, text_objects, death_zones