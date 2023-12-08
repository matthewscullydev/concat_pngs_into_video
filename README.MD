### Png into MKV Slideshow Script
---

USAGE

cd /directory/with/pictures

## move pngs to seperate folder before using script
mv $(ls | grep *.png) currently_pngs


png_rename_files_in_directory /directory/with/pictures

shuffle_files /directory/with/pictures

enter video output name

---

rename_directory.py

script for taking a directory of png | jpg | jpeg files and converting
them to png format and assigning a sequence number.

shuffle_files.py

script for taking these png files and reassigning them numbers in a subdirectory (functions as a random seed)

from here the subdirectory is passed into the argument for the bash script concat-video.sh

concat-video.sh

This script takes the files in the subdirectory and concats them into a video.

The time the images are shown in the video for can be modified!

this powerful script can modify the amount of time the images are shown before switching
