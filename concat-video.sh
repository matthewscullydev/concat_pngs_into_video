#!/bin/bash

# Check if the input folder argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <input_folder>"
    exit 1
fi

# Set the input folder from the command line argument
input_folder="$1"

# Check if the input folder exists
if [ ! -d "$input_folder" ]; then
    echo "Error: The specified folder does not exist."
    exit 1
fi

# Ask the user for the output video file
read -p "Enter the name for the output video file (without extension): " output_name

# Set the output video file with .mkv extension
output_video="$output_name.mkv"

# Check if the output video file already exists
if [ -e "$output_video" ]; then
    echo "Error: Output video file already exists. Please choose a different name."
    exit 1
fi

# Create a temporary directory for the images
temp_image_dir=$(mktemp -d)

# Create a set to keep track of unique images
unique_images=()

# Copy unique PNG images to the temporary directory and rename them
find "$input_folder" -type f -iname '*.png' -print0 |
    while IFS= read -r -d '' image; do
        md5sum_value=$(md5sum "$image" | cut -d" " -f1)
        if ! [[ " ${unique_images[@]} " =~ " $md5sum_value " ]]; then
            unique_images+=("$md5sum_value")
            cp "$image" "$temp_image_dir/$(basename "$image" | md5sum | cut -d" " -f1).png"
        fi
    done

# Use ffmpeg to concatenate unique PNG images into a random order MKV video
ffmpeg -r 1 -f image2 -pattern_type glob -i "$temp_image_dir/*.png" \
       -c:v libx264 -r 30 -pix_fmt yuv420p -analyzeduration 2147483647 -probesize 2147483647 "$output_video"

# Clean up the temporary image directory
rm -r "$temp_image_dir"

echo "Video creation complete. Output: $output_video"
