import os
import shutil

# Define the path to your downloads folder
download_path = os.path.expanduser("~/Downloads")

# Dictionary mapping folder names to their file extensions
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Installers": [".exe", ".msi"]
}

def organize_downloads():
    for filename in os.listdir(download_path):
        filepath = os.path.join(download_path, filename)
        
        # Skip directories, only process files
        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1].lower()
            
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(download_path, folder)
                    
                    # Create the folder if it doesn't exist
                    os.makedirs(dest_folder, exist_ok=True)
                    
                    # Move the file
                    shutil.move(filepath, os.path.join(dest_folder, filename))
                    print(f"Moved {filename} to {folder}")

if __name__ == "__main__":
    organize_downloads()