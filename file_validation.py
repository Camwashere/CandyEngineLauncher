

def find_dll_write_to_file(file_dir, output_file, input_extension='dll'):
    import os
    import glob

    if not input_extension.startswith('*.'):
        input_extension = '*.' + input_extension
    file_path = os.path.join(file_dir, input_extension)
    files = glob.glob(file_path)
    with open(output_file, "w") as f:
        for file in files:
            f.write(os.path.basename(file) + "\n")



