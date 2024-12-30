# game_engine/engine.py
import pygame
import sys

class GameEngine:
    def __init__(self):
        print("GameEngine initialized.")

    def run(self):
        print("Game is running...")

    def init(self):
        """ Initialize the game engine """
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        """ Handle user input and system events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """ Update game logic, such as movement or actions """
        for obj in self.objects:
            obj.update()

    def render(self):
        """ Render game objects to the screen """
        self.screen.fill((0, 0, 0))  # Clear the screen with black (no background image)
        for obj in self.objects:
            obj.render(self.screen)  # Each object handles its own rendering
        pygame.display.flip()  # Update the screen

    def run(self):
        """ Main game loop """
        self.init()

        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Set the frame rate (60 FPS)

        pygame.quit()
        sys.exit()
