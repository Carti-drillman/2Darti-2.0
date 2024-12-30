# main.py

import tkinter as tk
from game_engine.project_manager import ProjectManager

def main():
    root = tk.Tk()
    app = ProjectManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
