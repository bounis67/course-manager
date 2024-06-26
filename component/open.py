from component.check import check_last_chapter
import os

def open_file(file_path):
    """
    Opens a file using the default program associated with its file type.

    Args:
        file_path (str): The path of the file to be opened.

    Raises:
        Exception: If there is an error opening the file.

    """
    try:
        os.system(f'start {file_path}')
    except Exception as e:
        print(f"Error opening file: {e}")



def open_folder(folder_path):
    """
    Opens the specified folder in the default file explorer.

    Args:
        folder_path (str): The path of the folder to be opened.

    Raises:
        Exception: If there is an error opening the folder.

    """
    try:
        # Use "explorer" on Windows to open a folder
        os.system(f'explorer {folder_path}')
        # For macOS, you can use "open": os.system(f'open {folder_path}')
        # For Linux, you can use "xdg-open": os.system(f'xdg-open {folder_path}')
    except Exception as e:
        print(f"Error opening folder: {e}")

def open_last_class(main_folder, year, subject):
    """
    Opens the last class document for a given year and subject.

    Args:
        main_folder (str): The main folder path.
        year (str): The year of the class.
        subject (str): The subject of the class.

    Returns:
        None
    """
    main_folder = os.path.join(main_folder, year, subject)

    last_chapter = check_last_chapter(main_folder)
    last_chapter = f"Chapter{last_chapter:02d}"
    main_folder = os.path.join(main_folder, last_chapter, f"{subject}_{last_chapter}_Lesson.docx")
    print(main_folder)
    open_file(main_folder)
