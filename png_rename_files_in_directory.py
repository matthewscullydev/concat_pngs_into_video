
import subprocess
import os
import sys

def convert_and_remove(directory_path):
    # Change to the directory
    os.chdir(directory_path)

    # Initialize a counter for sequential numbering
    counter = 1

    # List to store files to be removed
    files_to_remove = []

    # Loop through each file in the directory
    for filename in os.listdir(directory_path):
        # Check if the file has a valid extension
        if filename.lower().endswith(('.jpeg', '.jpg')):
            # Construct the new PNG filename with sequential numbering
            new_filename = f"{counter}.png"

            # Use ffmpeg to convert the image to PNG format
            subprocess.run(["ffmpeg", "-i", filename, new_filename])

            # Add the original file to the list of files to be removed
            files_to_remove.append(filename)

            # Increment the counter
            counter += 1
        elif filename.lower().endswith('.png'):
            # If the file is already a PNG, increment the counter without conversion
            counter += 1

    # Remove the original JPEG or JPG files
    for file_to_remove in files_to_remove:
        os.remove(file_to_remove)

if __name__ == "__main__":
    # Check if a directory path is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    convert_and_remove(directory_path)
