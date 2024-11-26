import pygame

def load_level():
    platforms = [
        pygame.Rect(0, 580, 380, 20),
        pygame.Rect(20, 400, 150, 20),
        pygame.Rect(70, 300, 100, 20),
        pygame.Rect(360, 500, 20, 20),
        pygame.Rect(560, 400, 20, 20), 
        pygame.Rect(700, 300, 20, 20),
        pygame.Rect(560, 200, 20, 20),
        pygame.Rect(460, 100, 20, 20), 
        pygame.Rect(100, 100, 150, 20),
        pygame.Rect(480, 500, 20, 20)

    ]
    spawn_point = (75, 550) 
    powerups = [
        pygame.Rect(190, 440, 20, 20)
    ]
    gate = pygame.Rect(160, 50, 30, 50)
    death_zones = [
        pygame.Rect(0, 0, 20, 600),
        pygame.Rect(380, 580 ,420, 20),
        pygame.Rect(150, 480, 20, 100),
        pygame.Rect(240, 300, 20, 280),
        pygame.Rect(300, 200, 20, 320),
        pygame.Rect(80, 380, 40, 20)
    ]
    text_objects = [
        {"content": "Good luck!", "position": (50, 500)}
    ]
    return platforms, powerups, gate, spawn_point, text_objects, death_zones