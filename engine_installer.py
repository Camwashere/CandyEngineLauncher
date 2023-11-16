import tkinter as tk
from tkinter import filedialog
import subprocess
import configparser
import os


def clone_engine_core(config, install_dir):
    repo_name = 'CandyEngine'
    repo_url = config['Core']['engine']
    directory = os.path.join(install_dir, repo_name)
    try:
        subprocess.check_call(['git', 'clone', repo_url, directory])
        return True
    except subprocess.CalledProcessError as err:
        print(f'Error while cloning {repo_name}: {err}')
        return False


def choose_install_directory():
    root = tk.Tk()  # create root window
    root.withdraw()  # hide root window

    engine_install_dir = filedialog.askdirectory(title="Select Candy Engine Install Directory")
    return engine_install_dir


def install_engine_core(install_dir):
    print("Installing engine...")
    # load ini file
    config = configparser.ConfigParser()
    config.read('links.ini')  # Change to your ini file path
    if not clone_engine_core(config, install_dir):
        print("Failed to clone engine core!")
        exit(1)

    root_dir = os.path.join(install_dir, 'CandyEngine')
    print(f'Root dir {root_dir}')
    return root_dir
