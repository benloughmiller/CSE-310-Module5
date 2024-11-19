import pygame

def load_level():
    platforms = [
        pygame.Rect(100, 500, 150, 200),
        pygame.Rect(300, 400, 150, 400),
        pygame.Rect(500, 300, 150, 600)
    ]
    spawn_point = (100, 475)
    powerups = [(600, 350)]
    gate = pygame.Rect(50, 100, 30, 50)
    return platforms, powerups, gate, spawn_point