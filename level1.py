import pygame

def load_level():
    platforms = [
        pygame.Rect(100, 500, 150, 200),
        pygame.Rect(300, 400, 150, 400),
        pygame.Rect(500, 300, 150, 600)
    ]
    spawn_point = (160, 475)
    powerups = []
    gate = pygame.Rect(560, 250, 30, 50)
    return platforms, powerups, gate, spawn_point
