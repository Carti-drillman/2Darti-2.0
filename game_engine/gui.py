import tkinter as tk
from tkinter import simpledialog, colorchooser, messagebox
import os
from game_engine._3d_renderer import Renderer3D  # Import the 3D renderer

class GameEngineGUI:
    def __init__(self, root, project_dir="projects"):
        self.root = root
        self.root.title("2Darti Game Engine")
        self.root.geometry("800x600")  # Size of the window
        self.project_dir = project_dir  # Directory for storing project files
        self.objects = []  # To store objects in the game
        self.selected_object = None  # For currently selected object for moving/scaling
        self.offset_x = 0
        self.offset_y = 0

        self.canvas = None
        self.renderer_3d = None  # Initialize 3D renderer

        # Create the initial 2D canvas
        self.create_2d_canvas()

        # Add main buttons
        self.add_buttons()

    def add_buttons(self):
        """ Add main buttons to the GUI. """
        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_game)
        self.exit_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.run_button = tk.Button(self.root, text="Run", command=self.run_game)
        self.run_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.save_button = tk.Button(self.root, text="Save as .DD File", command=self.save_game)
        self.save_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.toggle_3d_button = tk.Button(self.root, text="Toggle 3D Mode", command=self.toggle_3d)
        self.toggle_3d_button.pack(side=tk.LEFT, padx=10, pady=10)

    def create_2d_canvas(self):
        """ Create the initial 2D canvas for the game engine. """
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=400)
        self.canvas.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)

    def toggle_3d(self):
        """ Toggle between 2D and 3D modes. """
        if self.renderer_3d is None:
            self.setup_3d()
        else:
            self.close_3d()

    def setup_3d(self):
        """ Set up the 3D renderer and switch the view. """
        self.renderer_3d = Renderer3D()
        self.root.after(10, self.renderer_loop)

    def close_3d(self):
        """ Close the 3D renderer and revert to 2D. """
        self.renderer_3d = None
        self.canvas.pack_forget()
        self.create_2d_canvas()

    def renderer_loop(self):
        """ Loop to keep rendering in 3D mode. """
        if self.renderer_3d:
            self.renderer_3d.run()

    def exit_game(self):
        """ Close the application. """
        self.root.quit()

    def run_game(self):
        """ Run or preview the game. """
        messagebox.showinfo("Run", "Game is running... (this is a placeholder)")

    def save_game(self):
        """ Save the game as a .DD file. """
        file_path = simpledialog.askstring("Save Game", "Enter file name to save as .dd:")
        if file_path:
            if not file_path.endswith(".dd"):
                file_path += ".dd"
            with open(file_path, 'w') as f:
                f.write("This is a placeholder for saving the project.")
            messagebox.showinfo("Save", f"Game saved as {file_path}")
