import os

# create directory
os.mkdir("test_dir")

# create nested directories
os.makedirs("test_dir/subdir", exist_ok=True)

# list files and folders
print("Files and folders:")
print(os.listdir("."))

# show current directory
print("Current directory:", os.getcwd())