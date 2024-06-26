import os

def check_last_chapter(main_directory):
    """
    Returns the number of the last chapter in the given directory.

    Parameters:
    - main_directory (str): The path to the main directory.

    Returns:
    - int: The number of the last chapter found in the directory.
    """
    existing_chapters = [f for f in os.listdir(
        main_directory) if f.startswith("Chapter") and f[8:].isdigit()]
    chapter_number = max([int(chapter[8:])
                          for chapter in existing_chapters], default=0)
    return chapter_number
