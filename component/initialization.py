import os
from component.creation import add_chapter_content

def initialize_project(main_folder, year, subjects):
    """
    Initializes a project by creating the main folder, year folder, and initializing subjects.

    Args:
        main_folder (str): Path of the main folder.
        year (str): Year of the project.
        subjects (list): List of subjects to initialize.

    Returns:
        None
    """

    # Path of the main folder "CoursFolder"

    # Check if the main folder exists, otherwise create it
    if not os.path.exists(main_folder):
        os.mkdir(main_folder)
        print(f'Main folder "{main_folder}" created.')

    # Path of the year folder
    year_folder = os.path.join(main_folder, year)

    # Check if the year folder exists, otherwise create it
    if not os.path.exists(year_folder):
        os.mkdir(year_folder)
        print(f'Year folder "{year}" created.')

    for subject in subjects:
        initialize_subject(year_folder, subject, main_folder, year)

    print("Initialization completed.")


def initialize_subject(year_folder, subject, main_folder, year):
    """
    Initializes a subject folder within a given year folder.

    Parameters:
    - year_folder (str): The path of the year folder.
    - subject (str): The name of the subject.
    - main_folder (str): The main folder containing the year folders.
    - year (str): The name of the year.

    Returns:
    None
    """

    # Path of the subject folder
    subject_folder = os.path.join(year_folder, subject)

    # Check if the subject folder exists, otherwise create it
    if not os.path.exists(subject_folder):
        os.mkdir(subject_folder)
        print(f'Subject folder "{subject}" created.')

    initialize_chapter(subject_folder, subject,
                       year_folder, main_folder, year)


def initialize_chapter(subject_folder, subject, year_folder, main_folder, year):
    """
    Initializes a chapter by creating a folder for the chapter if it doesn't exist.

    Args:
        subject_folder (str): The path to the subject folder.
        subject (str): The name of the subject.
        year_folder (str): The path to the year folder.
        main_folder (str): The path to the main folder.
        year (str): The year of the chapter.

    Returns:
        None
    """
    chapter_subject = f'Chapter01'
    # Path of the chapter folder
    chapter_folder = os.path.join(subject_folder, chapter_subject)

    # Check if the chapter folder exists, otherwise create it
    if not os.path.exists(chapter_folder):
        os.mkdir(chapter_folder)
        print(
            f'Chapter folder "{chapter_subject}" created for subject "{subject}".')

    add_chapter_content(
        main_folder, year, subject, chapter_subject)
