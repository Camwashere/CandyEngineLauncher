import tkinter as tk

import project_loader
import launcher_data as ld
import engine_installer
import file_validation

file_validation.find_dll_write_to_file("C:/Users/perso/CLionProjects/CandyEngine/build/debug", "requiredDLL.txt")

launcher_data = ld.load_launcher_data()

if launcher_data.needs_engine_install():
    print("Needs engine install")
    engine_installer.launch_installer()

else:
    print("Does not need engine install")

root = tk.Tk()
root.title("Candy Engine Launcher")

if launcher_data.has_projects():
    project_loader.launch_project_loader(root, launcher_data.known_project_dirs)

root.mainloop()
