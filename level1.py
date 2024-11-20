import pygame

def load_level():
    platforms = [
        pygame.Rect(100, 500, 150, 20),
        pygame.Rect(300, 400, 150, 20),
        pygame.Rect(500, 300, 150, 20)
    ]
    spawn_point = (160, 475)
    powerups = []
    gate = pygame.Rect(560, 250, 30, 50)
    death_zones = [
        pygame.Rect(0, 580, 800, 20)
    ]
    text_objects = [
        {"content": "Move with the Arrow Keys", "position": (30, 300)},
        {"content": "Press Space to jump", "position": (50, 330)}
    ]
    return platforms, powerups, gate, spawn_point, text_objects, death_zones
