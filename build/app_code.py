This script is not intended to be run from a command line, rather in the supplied app. 

The app, when run, will prompt the user to 
1. select a source directory: The folder in which all testResult sub-folders can be found. It is vital that the  VOC samples are processed in chronological order
2. select a target directory: The folder in which the renamed testResult files will be placed

"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog

def rename_and_move_files(source_dir, target_dir):
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Count the number of sub-folders
    subfolders = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))]
    num_subfolders = len(subfolders)
    subfolders.sort()


    # Iterate through sub-folders and rename .txt files
    for folder_num, folder in enumerate(subfolders, start=1):
        folder_path = os.path.join(source_dir, folder)
        txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt') and 'Test_1' not in f]

        for txt_file in txt_files:
            old_file_path = os.path.join(folder_path, txt_file)
            new_file_name = f'D{folder_num}_{txt_file}'
            new_file_path = os.path.join(target_dir, new_file_name)

            # Rename and move the file to the target directory
            shutil.copy2(old_file_path, new_file_path)

    print(f'Renamed and moved {num_subfolders} sub-folders worth of .txt files.')


# Function to get source and target directories using tkinter
def get_directories():
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    # Ask the user to select the source directory
    source_dir = filedialog.askdirectory(title="Select Source Directory")

    # Ask the user to select the target directory
    target_dir = filedialog.askdirectory(title="Select Target Directory")

    # Check if the user canceled the selection
    if not source_dir or not target_dir:
        return None, None  # User canceled the selection
    else:
        return source_dir, target_dir

# Get source and target directories using the function


if __name__ == "__main__":
    source_dir, target_dir = get_directories()

    # Check if the user canceled the selection
    if source_dir is None or target_dir is None:
        print("Selection canceled by user.")
    else:
        print("Source Directory:", source_dir)
        print("Target Directory:", target_dir)

        rename_and_move_files(source_dir, target_dir)  # Move this inside the else block
