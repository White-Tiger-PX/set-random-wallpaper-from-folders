import random
import ctypes

from pathlib import Path

import config


def is_valid_image(file_path, image_extensions):
    """
    Checks if a file is an image based on its extension.
    """
    return file_path.suffix.lower() in image_extensions


def select_random_existing_image(folder, include_subfolders, image_extensions):
    """
    Selects a random image from the specified folder and subfolders (if enabled).
    """
    search_pattern = '**/*' if include_subfolders else '*'
    images = [
        file
        for file in Path(folder).glob(search_pattern)
        if file.is_file() and is_valid_image(file, image_extensions)
    ]

    if not images:
        raise Exception(f"No images found in the folder: {folder}.")

    return random.choice(images)


def set_wallpaper(image_path):
    """
    Sets the specified image as the desktop wallpaper.
    """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(image_path), 3)


def main():
    """
    Main function to select and set a random image from the folders.
    """
    try:
        # Get configuration data
        FOLDERS = config.FOLDERS
        IMAGE_EXTENSIONS = config.IMAGE_EXTENSIONS

        # Choose a random folder from the list
        selected_folder = random.choice(FOLDERS)
        folder_path = selected_folder["path"]
        include_subfolders = selected_folder["include_subfolders"]

        # Select a random image from the chosen folder
        selected_image = select_random_existing_image(
            folder_path, include_subfolders, IMAGE_EXTENSIONS
        )

        # Set the selected image as the wallpaper
        set_wallpaper(selected_image)
        print(f"Wallpaper set to: {selected_image}")

    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    main()
