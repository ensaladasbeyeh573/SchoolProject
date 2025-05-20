import os
import shutil

def move_files(src_dir, dst_dir):
    # Move all files from src_dir to dst_dir
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dst_dir, filename)
        shutil.move(src_file, dst_file)

# Example usage:
src_dir = "path/to/source/directory"  # Replace with the path to your source directory
dst_dir = "path/to/destination/directory"  # Replace with the desired destination directory

move_files(src_dir, dst_dir)
