# game_engine/editor.py

import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import os

class GameEditor:
    def __init__(self, root, project_path):
        self.root = root
        self.root.title("2Darti Game Editor")
        self.root.geometry("800x600")
        self.project_path = project_path  # Path to the project

        # Canvas for the game objects
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=500)
        self.canvas.pack(pady=10)
        
        # Label to display project path
        self.project_label = tk.Label(self.root, text=f"Editing Project: {project_path}")
        self.project_label.pack()

        # Buttons at the top (EXIT, RUN, SAVE AS .DD FILE, SETTINGS, SCRIPT)
        self.top_buttons_frame = tk.Frame(self.root)
        self.top_buttons_frame.pack(pady=10)

        self.exit_button = tk.Button(self.top_buttons_frame, text="EXIT", command=self.exit_editor)
        self.exit_button.pack(side="left", padx=5)
        
        self.run_button = tk.Button(self.top_buttons_frame, text="RUN", command=self.run_game)
        self.run_button.pack(side="left", padx=5)
        
        self.save_button = tk.Button(self.top_buttons_frame, text="SAVE AS .DD FILE", command=self.save_game)
        self.save_button.pack(side="left", padx=5)
        
        self.settings_button = tk.Button(self.top_buttons_frame, text="SETTINGS", command=self.open_settings)
        self.settings_button.pack(side="left", padx=5)
        
        self.script_button = tk.Button(self.top_buttons_frame, text="SCRIPT", command=self.open_script_editor)
        self.script_button.pack(side="left", padx=5)

        # Add Object Button
        self.add_object_button = tk.Button(self.root, text="Add Object", command=self.open_add_object_window)
        self.add_object_button.pack(pady=20)

        # Add Text Button
        self.add_text_button = tk.Button(self.root, text="Add Text", command=self.open_add_text_window)
        self.add_text_button.pack(pady=5)

        # Delete Object Button
        self.delete_object_button = tk.Button(self.root, text="Delete Object", command=self.delete_object)
        self.delete_object_button.pack(pady=5)

        # List of objects on the canvas
        self.objects = []  # Will hold all objects on the canvas (rectangles, circles, texts)
        self.selected_object = None  # Track the currently selected object for movement or editing
        
        # Bind the canvas mouse events
        self.canvas.bind("<Button-1>", self.select_object)
        self.canvas.bind("<B1-Motion>", self.move_object)

    def exit_editor(self):
        """ Close the editor """
        self.root.quit()
        
    def run_game(self):
        """ Placeholder function to run the game """
        messagebox.showinfo("Run Game", "Running the game (this is just a placeholder).")

    def save_game(self):
        """ Placeholder function to save the game as .DD file """
        file_path = filedialog.asksaveasfilename(defaultextension=".dd", filetypes=[("Game Files", "*.dd")])
        if file_path:
            messagebox.showinfo("Save Game", f"Game saved as: {file_path}")
        
    def open_settings(self):
        """ Placeholder function for settings """
        messagebox.showinfo("Settings", "Settings (this is just a placeholder).")
        
    def open_script_editor(self):
        """ Open the script editor where the user can write code """
        self.script_editor_window = tk.Toplevel(self.root)
        self.script_editor_window.title("Script Editor")
        self.script_editor_window.geometry("600x400")
        
        self.script_text = tk.Text(self.script_editor_window, wrap=tk.WORD, height=20, width=60)
        self.script_text.pack(padx=10, pady=10)
        
        save_button = tk.Button(self.script_editor_window, text="Save Script", command=self.save_script)
        save_button.pack(pady=10)
        
    def save_script(self):
        """ Save the script written in the script editor """
        script_content = self.script_text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(script_content)
            messagebox.showinfo("Save Script", f"Script saved as: {file_path}")
    
    def open_add_object_window(self):
        """ Open a window to add a new object (rectangle) to the canvas """
        self.add_object_window = tk.Toplevel(self.root)
        self.add_object_window.title("Add New Object")
        
        # Name Entry
        tk.Label(self.add_object_window, text="Name:").pack()
        self.object_name = tk.Entry(self.add_object_window)
        self.object_name.pack()
        
        # Shape Selection
        tk.Label(self.add_object_window, text="Shape:").pack()
        self.shape_var = tk.StringVar(value="Rectangle")
        self.shape_menu = tk.OptionMenu(self.add_object_window, self.shape_var, "Rectangle", "Circle")
        self.shape_menu.pack()

        # Color Selection
        tk.Label(self.add_object_window, text="Color:").pack()
        self.color_var = tk.StringVar(value="blue")
        self.color_menu = tk.OptionMenu(self.add_object_window, self.color_var, "blue", "red", "green", "yellow", "black")
        self.color_menu.pack()

        # Width and Height for shape dimensions
        tk.Label(self.add_object_window, text="Width:").pack()
        self.width_entry = tk.Entry(self.add_object_window)
        self.width_entry.pack()

        tk.Label(self.add_object_window, text="Height:").pack()
        self.height_entry = tk.Entry(self.add_object_window)
        self.height_entry.pack()

        # Submit Button
        submit_button = tk.Button(self.add_object_window, text="Add", command=self.add_object)
        submit_button.pack(pady=10)

    def add_object(self):
        """ Add an object (rectangle or circle) to the canvas """
        name = self.object_name.get()
        shape = self.shape_var.get()
        color = self.color_var.get()
        
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Width and Height must be integers.")
            return
        
        if shape == "Rectangle":
            obj_id = self.canvas.create_rectangle(50, 50, 50 + width, 50 + height, fill=color)
        elif shape == "Circle":
            obj_id = self.canvas.create_oval(50, 50, 50 + width, 50 + height, fill=color)

        # Store the object
        self.objects.append({
            "name": name,
            "id": obj_id,
            "shape": shape,
            "color": color,
            "width": width,
            "height": height
        })
        
        messagebox.showinfo("Success", f"{shape} '{name}' added to the canvas!")
        self.add_object_window.destroy()

    def open_add_text_window(self):
        """ Open a window to add text to the canvas """
        self.add_text_window = tk.Toplevel(self.root)
        self.add_text_window.title("Add Text")
        
        # Text Content Entry
        tk.Label(self.add_text_window, text="Text:").pack()
        self.text_content = tk.Entry(self.add_text_window)
        self.text_content.pack()

        # Font Size
        tk.Label(self.add_text_window, text="Font Size:").pack()
        self.font_size = tk.Entry(self.add_text_window)
        self.font_size.pack()

        # Color Selection
        tk.Label(self.add_text_window, text="Text Color:").pack()
        self.text_color = tk.StringVar(value="black")
        self.text_color_menu = tk.OptionMenu(self.add_text_window, self.text_color, "black", "blue", "red", "green")
        self.text_color_menu.pack()

        # Submit Button
        submit_button = tk.Button(self.add_text_window, text="Add Text", command=self.add_text)
        submit_button.pack(pady=10)

    def add_text(self):
        """ Add text to the canvas """
        text = self.text_content.get()
        try:
            font_size = int(self.font_size.get())
        except ValueError:
            messagebox.showerror("Error", "Font size must be an integer.")
            return
        
        color = self.text_color.get()
        
        text_id = self.canvas.create_text(50, 50, text=text, fill=color, font=("Helvetica", font_size))

        # Store the text object
        self.objects.append({
            "name": text,
            "id": text_id,
            "shape": "Text",
            "color": color,
            "font_size": font_size,
            "text": text
        })
        
        messagebox.showinfo("Success", f"Text '{text}' added to the canvas!")
        self.add_text_window.destroy()

    def select_object(self, event):
        """ Select an object when clicked """
        for obj in self.objects:
            item = obj["id"]
            if self.canvas.bbox(item):
                x1, y1, x2, y2 = self.canvas.bbox(item)
                if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                    self.selected_object = obj
                    break

    def move_object(self, event):
        """ Move the selected object by dragging it """
        if self.selected_object:
            item = self.selected_object["id"]
            dx = event.x - (self.canvas.bbox(item)[0] + self.canvas.bbox(item)[2]) / 2
            dy = event.y - (self.canvas.bbox(item)[1] + self.canvas.bbox(item)[3]) / 2
            self.canvas.move(item, dx, dy)

    def delete_object(self):
        """ Delete the selected object """
        if self.selected_object:
            self.canvas.delete(self.selected_object["id"])
            self.objects.remove(self.selected_object)
            self.selected_object = None
            messagebox.showinfo("Success", "Object deleted!")
        else:
            messagebox.showerror("Error", "No object selected to delete.")