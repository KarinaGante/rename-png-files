import tkinter as tk
from tkinter import filedialog, messagebox
import os


def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        rename_files(folder)


def rename_files(folder):
    arq_list = os.listdir(folder)
    arq_list.sort()

    default_paths = {}

    for i, arq_name in enumerate(arq_list):
        default_path = os.path.join(folder, arq_name)
        new_name = os.path.join(folder, f"{i + 1}.png")
        new_path = os.path.join(folder, new_name)
        os.rename(default_path, new_path)
        default_paths[new_path] = default_path

    show_alert(default_paths)


def undo_renaming(default_paths):
    for new_path, default_path in default_paths.items():
        os.rename(new_path, default_path)
    messagebox.showinfo("Renaming Undone", "Rename successed undone!")


def show_alert(default_paths):
    resp = messagebox.askquestion(
        "Renaming Done", "Files successed renamed!\nDo you want to undo renaming?")
    if resp == "yes":
        undo_renaming(default_paths)
    root.destroy()


root = tk.Tk()
root.title("Renaming png files")

window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

botao = tk.Button(root, text="Select local folder", command=select_folder)
botao.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()