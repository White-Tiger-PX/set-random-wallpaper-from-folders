<p align="center">
  <a href="README.ru.md"><img src="https://img.shields.io/badge/Русский-Readme-blue" alt="Russian" /></a>&nbsp;&nbsp;
  <a href="README.md"><img src="https://img.shields.io/badge/English-Readme-blue" alt="English" /></a>&nbsp;&nbsp;
  <img src="https://visitor-badge.laobi.icu/badge?page_id=White-Tiger-PX.set-random-wallpaper-from-folders" alt="visitors" />&nbsp;&nbsp;
  <img src="https://img.shields.io/github/stars/White-Tiger-PX/set-random-wallpaper-from-folders?style=social" alt="GitHub stars" />
</p>

# set-random-wallpaper-from-folders

This script allows you to set a random image from a specified list of folders as your desktop wallpaper. It supports filtering by image extensions and includes options to search in subfolders.

## Features

- Selects a random image from one or more specified folders.
- Supports filtering by file extension.
- Option to include or exclude subfolders in the search.
- Automatically sets the selected image as the desktop wallpaper.

## Supported Operating Systems

This script is designed specifically for Windows. It uses the ctypes library to interact with the Windows API and set the desktop wallpaper.

## Setup

### Configure Image Folders

- Open the `config.py` file.
- Replace the paths in the `FOLDERS` list with the directories containing your images.
- For each folder, you can specify whether to include subfolders in the search by setting `include_subfolders` to `True` or `False`.

### Automate the Script Execution

To run the script automatically on system startup, set up a task in Windows Task Scheduler:

1. Open the **Task Scheduler** by searching for **Task Scheduler** in the Start menu (or press `Win + R`, type `taskschd.msc`, and press Enter).
2. Click on **Create task** in the right-hand panel.
3. Provide a name for your task (e.g., "Set Random Wallpaper").
4. Go to the **Triggers** tab, and click **New**.
   - Set the **Begin the task** option to **At logon** to ensure the task starts whenever you log into your system.
   - Optionally, check **Repeat task every** and set the interval (e.g., every 1 hour), if you want the task to run periodically.
5. Go to the **Actions** tab, click **New**, and choose **Start a Program**.
6. Browse and select the Python executable. By default, it is located at:
   `C:\Users\YOU_USERNAME\AppData\Local\Programs\Python\YOU_VERSION_python\python.exe`.
7. In the **Add arguments** field, provide the full path to your script. For example:
   `(C:\path\to\your\set_random_wallpaper_from_folders.py)`
   *(Ensure the path is in quotes if it contains spaces.)*
8. Click **OK** to save the task.

<div style="justify-content: space-between; align-items: center;">
  <div style="text-align: center;">
    <img src="Task Scheduler - General.png" alt="Task Scheduler - General" width="75%" />
  </div>

  <div style="text-align: center;">
    <img src="Task Scheduler - Triggers.png" alt="Task Scheduler - Triggers" width="75%" />
  </div>

  <div style="text-align: center;">
    <img src="Task Scheduler - Actions.png" alt="Task Scheduler - Actions" width="75%" />
  </div>
</div>
