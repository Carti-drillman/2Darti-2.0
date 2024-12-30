# game_engine/game_object.py
import pygame

class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color  # RGB color tuple (255, 0, 0) for red

    def update(self):
        """ Update game object logic (e.g., movement) """
        pass

    def render(self, screen):
        """ Render the object as a rectangle on the screen """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
