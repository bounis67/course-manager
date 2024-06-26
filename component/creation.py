import os
import shutil


def add_chapter_content(main_directory, year, subject, chapter):
    """
    Creates chapter content for a given subject and chapter.

    Args:
        main_directory (str): The main directory path.
        year (str): The year of study.
        subject (str): The subject name.
        chapter (str): The chapter name.

    Returns:
        None
    """
    subchapter_files = ["Cours.docx"]
    for file in subchapter_files:
        chapter_subject_directory = os.path.join(
            main_directory, year, subject, chapter)

        os.makedirs(chapter_subject_directory, exist_ok=True)

        reference_file_path = os.path.join(
            main_directory, "script\\component\\file\\file_docx.docx")
        destination_file_name = f'{subject}_{chapter}_{file[:-5]}.docx'
        destination_file_path = os.path.join(
            chapter_subject_directory, destination_file_name)

        if not os.path.exists(destination_file_path):
            shutil.copy(reference_file_path, destination_file_path)
            print(
                f'File "{file}" created under chapter "{chapter}" for subject "{subject}".')

    subchapter_directories = ["Control", "Exercise", "Other"]
    for directory in subchapter_directories:
        subchapter_directory = os.path.join(
            chapter_subject_directory, directory)
        if not os.path.exists(subchapter_directory):
            os.makedirs(subchapter_directory)
            print(
                f'Directory "{directory}" created under chapter "{chapter}" for subject "{subject}".')


def add_chapter(main_directory, year, subject):
    """
    Add a new chapter to the specified subject and year.

    Args:
        main_directory (str): The main directory path.
        year (str): The year of the subject.
        subject (str): The subject name.

    Returns:
        None
    """
    # Get the subject directory path
    subject_directory = os.path.join(main_directory, year, subject)

    # Get the existing chapters in the subject directory
    existing_chapters = [f for f in os.listdir(
        subject_directory) if f.startswith("Chapter") and f[8:].isdigit()]

    # Find the highest chapter number
    last_chapter = max([int(chapter[8:])
                       for chapter in existing_chapters], default=0)

    # Create the name for the new chapter in a unique way
    new_chapter = f"Chapter{last_chapter + 1:02d}"

    # Create the directory for the new chapter
    new_chapter_path = os.path.join(subject_directory, new_chapter)

    # Check if the directory already exists, if so, add a numeric suffix
    i = 1
    while os.path.exists(new_chapter_path):
        new_chapter = f"Chapter{last_chapter + i:02d}"
        new_chapter_path = os.path.join(subject_directory, new_chapter)
        i += 1

    os.mkdir(new_chapter_path)

    print(f"Chapter added: {new_chapter}")
    add_chapter_content(main_directory, year, subject, new_chapter)


def add_control(main_directory, year, subject, chapter):
    """
    Create a new control folder and copy a reference file into it.

    Args:
        main_directory (str): The main directory path.
        year (str): The year.
        subject (str): The subject.
        chapter (str): The chapter.

    Returns:
        None
    """
    control_directory = os.path.join(
        main_directory, year, subject, chapter, "control")

    # Filter the items in the subject folder that start with "Control" and have a number
    existing_controls = [f for f in os.listdir(
        control_directory) if f.startswith("Control") and f[7:].isdigit()]

    # Find the number of the last control
    last_control = max([int(control[7:])
                       for control in existing_controls], default=0)

    # Create the name of the new control in a unique way
    new_control = f"Control{last_control + 1:02d}"

    # Create the directory for the new control
    new_control_path = os.path.join(control_directory, new_control)

    # Check if the directory already exists, if so, add a numeric suffix
    i = 1
    while os.path.exists(new_control_path):
        new_control = f"Control{last_control + i:02d}"
        new_control_path = os.path.join(control_directory, new_control)
        i += 1

    os.mkdir(new_control_path)

    print(f"Added control folder: {new_control}")

    # Copy the reference file and rename it
    reference_file = os.path.join(
        main_directory, "script\\component\\file\\file_docx.docx")
    destination_file_name = f"{new_control}_{
        subject}_{chapter}_Boehm_Corentin.docx"
    destination_file_path = os.path.join(
        new_control_path, destination_file_name)

    if not os.path.exists(destination_file_path):
        shutil.copy(reference_file, destination_file_path)
        print(
            f'Created "Control" file for subject "{subject}" under control "{new_control}".')


def add_exercise(main_directory, year, subject, chapter):
    """
    Create a new exercise directory and copy a reference file into it.

    Args:
        main_directory (str): The main directory path.
        year (str): The year of the exercise.
        subject (str): The subject of the exercise.
        chapter (str): The chapter of the exercise.

    Returns:
        None
    """
    exercise_directory = os.path.join(
        main_directory, year, subject, chapter, "Exercise")

    # Filter the items in the subject folder that start with "Exercise" and have a number
    existing_exercises = [f for f in os.listdir(
        exercise_directory) if f.startswith("Exercise") and f[8:].isdigit()]

    # Find the number of the last exercise
    last_exercise = max([int(exercise[8:])
                        for exercise in existing_exercises], default=0)

    # Create the name of the new exercise in a unique way
    new_exercise = f"Exercise{last_exercise + 1:02d}"

    # Create the directory for the new exercise
    new_exercise_path = os.path.join(exercise_directory, new_exercise)

    # Check if the directory already exists, if so, add a numeric suffix
    i = 1
    while os.path.exists(new_exercise_path):
        new_exercise = f"Exercise{last_exercise + i:02d}"
        new_exercise_path = os.path.join(exercise_directory, new_exercise)
        i += 1

    os.mkdir(new_exercise_path)

    print(f"Added exercise folder: {new_exercise}")

    # Copy the reference file and rename it
    reference_file = os.path.join(
        main_directory, "script\\component\\file\\file_docx.docx")
    destination_file_name = f"{new_exercise}_{
        subject}_{chapter}_Boehm_Corentin.docx"
    destination_file_path = os.path.join(
        new_exercise_path, destination_file_name)

    if not os.path.exists(destination_file_path):
        shutil.copy(reference_file, destination_file_path)
        print(
            f'Created "Exercise" file for subject "{subject}" under exercise "{new_exercise}".')
