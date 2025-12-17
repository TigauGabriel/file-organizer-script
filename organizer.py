import os
import shutil

# --- CONFIGURATION ---
# IMPORTANT: Replace this path with the folder you want to clean up.
# Use double backslashes (\\) or a raw string (r'...') for Windows paths.
target_directory = r'C:\Users\Gabi\Desktop\portofoliu_python\test_organizer'

# Dictionary mapping folder names to file extensions
EXTENSIONS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
    'Audio': ['.mp3', '.wav', '.flac'],
    'Video': ['.mp4', '.mkv', '.mov', '.avi'],
    'Archives': ['.zip', '.rar', '.7z', '.tar'],
    'Executables': ['.exe', '.msi']
}

def organize_files():
    print(f"Scanning directory: {target_directory}...")
    
    # Check if directory exists
    if not os.path.exists(target_directory):
        print("Error: The specified directory does not exist.")
        return

    # Get all files in the directory
    files = [f for f in os.listdir(target_directory) if os.path.isfile(os.path.join(target_directory, f))]
    
    moved_count = 0

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension.lower()
        
        # Find the correct category for this file
        destination_folder = None
        for category, exts in EXTENSIONS.items():
            if extension in exts:
                destination_folder = category
                break
        
        # If no category matches, skip or move to 'Others' (optional)
        if destination_folder:
            # Create the category folder if it doesn't exist
            folder_path = os.path.join(target_directory, destination_folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Move the file
            src_path = os.path.join(target_directory, file)
            dst_path = os.path.join(folder_path, file)
            
            try:
                shutil.move(src_path, dst_path)
                print(f"Moved: {file} -> {destination_folder}/")
                moved_count += 1
            except Exception as e:
                print(f"Error moving {file}: {e}")

    print(f"\nSuccess! Organized {moved_count} files.")

if __name__ == '__main__':
    organize_files()