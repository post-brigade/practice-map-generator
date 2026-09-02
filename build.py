from pathlib import Path

# Define directory structure
directories = [
    Path("src"),
]

# Create directories
for directory in directories:
    directory.mkdir(parents=True, exist_ok=True)

# Create initial empty files
files = [
    Path("src/main.py"),
    Path("README.md"),
]

for file_path in files:
    file_path.touch(exist_ok=True)
