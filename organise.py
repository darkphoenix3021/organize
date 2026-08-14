import shutil
from pathlib import Path

# 1. Define the categories and their associated file extensions
FILE_CATEGORIES = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".svg", ".heic"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".csv", ".pptx", ".ppt"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".html", ".css", ".js", ".json", ".cpp", ".java"],
    "Executables": [".exe", ".msi", ".dmg", ".pkg"]
}

def organize_directory(base_path):
    base_dir = Path(base_path)
    
    # Check if the path is valid
    if not base_dir.exists() or not base_dir.is_dir():
        print(f"Error: '{base_path}' is not a valid directory.")
        return

    # 2. Map every extension to its corresponding folder name
    ext_to_folder = {}
    for folder_name, extensions in FILE_CATEGORIES.items():
        for ext in extensions:
            ext_to_folder[ext] = folder_name

    count = 0
    
    # 3. Iterate through all items in the directory
    for file_path in base_dir.iterdir():
        # Skip directories, we only want to move files
        if file_path.is_file():
            # Get the file extension in lowercase (e.g., '.jpg')
            ext = file_path.suffix.lower()
            
            # Find the category folder, default to "Others" if not found
            folder_name = ext_to_folder.get(ext, "Others")
            
            # Create the destination directory if it doesn't exist
            dest_dir = base_dir / folder_name
            dest_dir.mkdir(exist_ok=True)
            
            dest_file_path = dest_dir / file_path.name

            # 4. Move the file
            try:
                # To avoid overwriting, check if a file with the same name already exists
                if dest_file_path.exists():
                    print(f"Skipped: '{file_path.name}' (File already exists in '{folder_name}')")
                else:
                    shutil.move(str(file_path), str(dest_file_path))
                    print(f"Moved: '{file_path.name}' -> {folder_name}/")
                    count += 1
            except Exception as e:
                print(f"Error moving '{file_path.name}': {e}")

    print(f"\nSuccess! Successfully organized {count} files.")

if __name__ == "__main__":
    print("=== Automated File Organizer ===")
    target_dir = input("Enter the absolute path of the folder to organize: ")
    organize_directory(target_dir)

