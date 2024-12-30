import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import os
import shutil
from game_engine.editor import GameEditor  # Import GameEditor from editor.py

class ProjectManager:
    def __init__(self, root):
        self.root = root
        self.root.title("2Darti Game Engine - Project Manager")
        self.root.geometry("400x300")
        
        self.project_dir = "projects"  # Directory where projects will be stored
        if not os.path.exists(self.project_dir):
            os.mkdir(self.project_dir)

        # Create Project Button
        self.create_button = tk.Button(self.root, text="Create Project", command=self.create_project)
        self.create_button.pack(pady=10)
        
        # Open Project Button
        self.open_button = tk.Button(self.root, text="Open Project", command=self.open_project)
        self.open_button.pack(pady=10)
        
        # Upload Project Button
        self.upload_button = tk.Button(self.root, text="Upload Project", command=self.upload_project)
        self.upload_button.pack(pady=10)
    
    def create_project(self):
        """ Function to create a new project directory """
        project_name = simpledialog.askstring("Project Name", "Enter project name:")
        if project_name:
            project_path = os.path.join(self.project_dir, project_name)
            if os.path.exists(project_path):
                messagebox.showerror("Error", f"Project '{project_name}' already exists.")
            else:
                try:
                    os.mkdir(project_path)  # Create the project folder
                    os.mkdir(os.path.join(project_path, "assets"))  # Create assets folder
                    os.mkdir(os.path.join(project_path, "scripts"))  # Create scripts folder
                    
                    # Create a basic game_script.py file
                    game_script = os.path.join(project_path, "scripts", "game_script.py")
                    with open(game_script, 'w') as f:
                        f.write("# Game script goes here\n")
                    
                    messagebox.showinfo("Success", f"Project '{project_name}' created successfully!")
                    
                    # Open the game editor window for this project
                    self.open_editor_window(project_path)

                except Exception as e:
                    messagebox.showerror("Error", f"Failed to create project: {e}")
        else:
            messagebox.showerror("Error", "Project name cannot be empty.")
    
    def open_project(self):
        """ Function to open an existing project directory """
        project_name = filedialog.askopenfilename(
            initialdir=self.project_dir, 
            title="Select a Project", 
            filetypes=[("Project Files", "*.dd")]
        )
        
        if project_name:
            # Extract project folder path from the selected .dd file
            project_path = os.path.dirname(project_name)
            self.open_editor_window(project_path)
        else:
            messagebox.showerror("Error", "No project selected.")
    
    def open_editor_window(self, project_path):
        """ Function to open the game editor window """
        print(f"Opening editor for project at {project_path}")  # Debugging line
        editor_root = tk.Tk()
        editor_app = GameEditor(editor_root, project_path)
        editor_app.run()

    def upload_project(self):
        """ Function to upload (move or zip) the project """
        project_name = simpledialog.askstring("Upload Project", "Enter project name to upload:")
        if project_name:
            project_path = os.path.join(self.project_dir, project_name)
            if os.path.exists(project_path):
                # Example: zip the project directory and move it
                zip_file = f"{project_name}.zip"
                zip_path = os.path.join(self.project_dir, zip_file)
                self.zip_directory(project_path, zip_path)
                messagebox.showinfo("Success", f"Project '{project_name}' uploaded as {zip_file}")
            else:
                messagebox.showerror("Error", f"Project '{project_name}' does not exist.")
        else:
            messagebox.showerror("Error", "Project name cannot be empty.")
    
    def zip_directory(self, dir_path, zip_name):
        """ Zips a directory into a zip file """
        import zipfile
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    zipf.write(os.path.join(root, file),
                               os.path.relpath(os.path.join(root, file), 
                                              os.path.join(dir_path, '..')))

# Main Program
def main():
    root = tk.Tk()
    app = ProjectManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
