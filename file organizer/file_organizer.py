import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
}

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if filename.lower().endswith(tuple(extensions)):
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    moved = True
                    break

            if not moved:  # Other file types
                other_folder = os.path.join(folder_path, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))

def bulk_rename(folder_path, prefix="file"):
    counter = 1
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1]
            new_name = f"{prefix}_{counter}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_path)
            counter += 1

def choose_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

def run_organize():
    path = folder_path.get()
    if not path:
        messagebox.showerror("Error", "Please select a folder.")
        return
    organize_files(path)
    messagebox.showinfo("Success", "Files organized successfully!")

def run_rename():
    path = folder_path.get()
    if not path:
        messagebox.showerror("Error", "Please select a folder.")
        return
    prefix = prefix_entry.get() or "file"
    bulk_rename(path, prefix)
    messagebox.showinfo("Success", f"Files renamed with prefix '{prefix}' successfully!")

# GUI Setup
root = tk.Tk()
root.title("File Organizer & Bulk Renamer")
root.geometry("400x250")
root.resizable(False, False)

folder_path = tk.StringVar()

tk.Label(root, text="Choose Folder:", font=("Arial", 12)).pack(pady=5)
tk.Entry(root, textvariable=folder_path, width=40).pack(pady=5)
tk.Button(root, text="Browse", command=choose_folder).pack(pady=5)

tk.Label(root, text="Rename Prefix:", font=("Arial", 12)).pack(pady=5)
prefix_entry = tk.Entry(root, width=20)
prefix_entry.pack(pady=5)

tk.Button(root, text="Organize Files", width=20, command=run_organize).pack(pady=10)
tk.Button(root, text="Bulk Rename Files", width=20, command=run_rename).pack(pady=5)

root.mainloop()
