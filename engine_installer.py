import tkinter as tk
from tkinter import filedialog

engine_github_url = "https://github.com/Camwashere/CandyEngine.git"


def install_engine(install_dir):
    print("Installing engine...")


def launch_installer():
    root = tk.Tk()  # create root window
    root.withdraw()  # hide root window

    engine_install_dir = filedialog.askdirectory(title="Select Candy Engine Install Directory")
    if not engine_install_dir:
        print("Engine installation directory is not selected.")
        exit(1)

    install_engine(engine_install_dir)
