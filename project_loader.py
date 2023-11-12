import os
import tkinter as tk


def get_projects(base_directory):
    projects = []
    for item in os.listdir(base_directory):
        item_path = os.path.join(base_directory, item)

        # check if it's a directory (project would be a directory)
        if os.path.isdir(item_path):
            # check if any `.candy` file exists in the directory
            if any(fname.endswith('.candy') for fname in os.listdir(item_path)):
                projects.append(item)
    return projects


def load_project(project):

    print("Loading project", project)


def launch_project_loader(root, available_projects):
    base_directory = "C:/Users/perso/CLionProjects/CandyEngine/build/debug/projects"
    print(f"Available Project Count: {len(available_projects)}")
    for project in available_projects:
        print(f"Project: {project}")

    # allow listbox to expand in grid
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)

    # create a title for the list
    label = tk.Label(root, text="Available Projects:")
    label.grid(row=0, column=0, sticky='w')

    # create a listbox
    listbox = tk.Listbox(root)
    listbox.grid(row=1, column=0, sticky='nsew')

    # add projects to listbox
    for project in available_projects:
        def load_selected_project(evt, p=project):
            load_project(p)
        listbox.insert(tk.END, project)

        # bind selection event to custom function
        listbox.bind('<Double-1>', load_selected_project)
