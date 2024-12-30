import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

class Renderer3D:
    def __init__(self, display=(800, 600)):
        self.display = display
        self.init_pygame()
        self.setup_camera()

    def init_pygame(self):
        """Initialize Pygame and set up the OpenGL window."""
        pygame.init()
        pygame.display.set_mode(self.display, pygame.DOUBLEBUF | pygame.OPENGL)
        
    def setup_camera(self):
        """Set up the perspective camera."""
        gluPerspective(45, (self.display[0] / self.display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
    
    def draw_cube(self):
        """Draw a 3D cube."""
        vertices = [
            [1, 1, -1],
            [1, -1, -1],
            [-1, -1, -1],
            [-1, 1, -1],
            [1, 1, 1],
            [1, -1, 1],
            [-1, -1, 1],
            [-1, 1, 1]
        ]
        edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]
        
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(vertices[vertex])
        glEnd()

    def update(self):
        """Update the scene, e.g., rotate the cube."""
        glRotatef(1, 3, 1, 1)  # Rotate the cube (1 degree per frame)
        
    def draw(self):
        """Draw the 3D scene."""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw_cube()
        pygame.display.flip()

    def run(self):
        """Start the rendering loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.update()
            self.draw()
            pygame.time.wait(10)  # Control the speed of the scene update
