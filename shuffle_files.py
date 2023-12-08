
import os
import random
import shutil
import subprocess
import sys

def shuffle_and_renumber_files(input_folder):
    # Get a list of all files in the input folder
    file_list = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpeg', '.jpg'))])

    # Shuffle the file list
    random.shuffle(file_list)

    # Create a new directory for the shuffled files
    output_folder = os.path.join(input_folder, "shuffled_files")
    os.makedirs(output_folder, exist_ok=True)

    # Copy and renumber the shuffled files to the new directory
    for index, filename in enumerate(file_list):
        file_extension = os.path.splitext(filename)[1].lower()
        new_filename = f"{index + 1}{file_extension}"
        shutil.copy2(os.path.join(input_folder, filename), os.path.join(output_folder, new_filename))

    print(f"Shuffling and renumbering complete. Shuffled files saved in {output_folder}")

    # Call concat-video.sh on the subdirectory
    concat_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "concat-video.sh")
    subprocess.run([concat_script_path, output_folder])

    # Remove the subdirectory
    shutil.rmtree(output_folder)
    print(f"Subdirectory {output_folder} removed.")

if __name__ == "__main__":
    # Check if a directory path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    input_folder = sys.argv[1]
    shuffle_and_renumber_files(input_folder)
