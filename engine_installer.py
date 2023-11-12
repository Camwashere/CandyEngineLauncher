import tkinter as tk
from tkinter import filedialog
import subprocess
import configparser
import os


def clone_engine_core(config, install_dir):
    repo_name = 'engine'
    repo_url = config['Core'][repo_name]
    directory = os.path.join(install_dir, repo_name)
    try:
        subprocess.check_call(['git', 'clone', repo_url, directory])
    except subprocess.CalledProcessError as err:
        print(f'Error while cloning {repo_name}: {err}')


def install_engine(install_dir):
    print("Installing engine...")
    # load ini file
    config = configparser.ConfigParser()
    config.read('file.ini')  # Change to your ini file path
    clone_engine_core(config, install_dir)


def launch_installer():
    root = tk.Tk()  # create root window
    root.withdraw()  # hide root window

    engine_install_dir = filedialog.askdirectory(title="Select Candy Engine Install Directory")
    if not engine_install_dir:
        print("Engine installation directory is not selected.")
        return

    install_engine(engine_install_dir)
