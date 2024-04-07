import os
import shutil

def sort_files(directory):
    try:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                file_extension = os.path.splitext(filename)[1][1:].lower()
                if file_extension:
                    target_folder = os.path.join(directory, file_extension)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    shutil.move(os.path.join(directory, filename), os.path.join(target_folder, filename))
        return f"Files in '{directory}' have been sorted into their respective folders."
    except Exception as e:
        return f"Error sorting files: {str(e)}"

# Example usage
directory_path = input("Enter the directory path to sort files: ")
result = sort_files(directory_path)
print(result)