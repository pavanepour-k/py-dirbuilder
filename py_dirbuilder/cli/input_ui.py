import os
import sys

def select_structure_file():
    print("\nEnter the path to the directory structure text file.")
    print("Press Enter to open file explorer.")
    path = input("Enter path (or press Enter): ").strip()
    if not path:
        # Windows file explorer integration
        if sys.platform.startswith('win'):
            try:
                import tkinter as tk
                from tkinter import filedialog
                root = tk.Tk(); root.withdraw()
                file_path = filedialog.askopenfilename(title="Select Structure File")
                if file_path:
                    return file_path
                else:
                    print("No file was selected.")
                    return None
            except Exception:
                print("Failed to open file explorer. Please enter the path manually.")
                return None
        else:
            print("File explorer not supported. Please enter the path manually.")
            return None
    if os.path.isfile(path):
        return path
    else:
        print("The specified file does not exist.")
        return None

def select_target_dir():
    print("\nEnter the path where directories will be created.")
    print("Press Enter to choose via file explorer.")
    path = input("Enter path (or press Enter): ").strip()
    if not path:
        if sys.platform.startswith('win'):
            try:
                import tkinter as tk
                from tkinter import filedialog
                root = tk.Tk(); root.withdraw()
                folder = filedialog.askdirectory(title="Select Target Directory")
                if folder:
                    return folder
                else:
                    print("No folder was selected.")
                    return None
            except Exception:
                print("Failed to open file explorer. Please enter the path manually.")
                return None
        else:
            print("File explorer not supported. Please enter the path manually.")
            return None
    return path if os.path.isdir(path) else None

def confirm(msg="Are you sure? (y/n): "):
    while True:
        ans = input(msg).strip().lower()
        if ans in {'y', 'yes'}:
            return True
        if ans in {'n', 'no'}:
            return False
        print("Please enter 'y' or 'n'.")
