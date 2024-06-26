from component.creation import add_chapter, add_chapter_content, add_control, add_exercise
from component.initialization import initialize_chapter, initialize_subject, initialize_project
from component.open import open_file, open_folder, open_last_class
from component.check import check_last_chapter
from component.calculation_tools import generate_numbers

import os


def get_user_choice(param):
    """
    Prompts the user for input and returns the user's choice as an integer.

    Args:
        param (str): The prompt message to display to the user.

    Returns:
        int: The user's choice as an integer.

    Raises:
        ValueError: If the user enters a non-integer value.
    """
    while True:
        try:
            user_choice = input(param)
            user_choice = int(user_choice)
            return user_choice
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    loop = True
    year = "1st"
    subjects = ["Mathematics", "French", "Computer Science", "History", "Geography",
                "Physics-Chemistry", "Social Studies", "English", "Civic Education"]
    choice = ""
    while loop == True:
        print("Choose the computer\n1) OneDrive \n2) Desktop")
        choice = input("> ")
        try:
            choice = int(choice)  # Convert the user input to an integer
            if choice == 1:
                main_folder = "C:\\Users\\BOUNIS\\OneDrive\\Desktop\\HighSchool"
                loop = False
            elif choice == 2:
                main_folder = "C:\\Users\\BOUNIS\\Desktop\\HighSchool"
                loop = False
            else:
                print("Please enter a valid number.")
        # except print error
        except Exception as e:
            print("Error: " + str(e))

    try:
        initialize_project(main_folder, year, subjects)
    except Exception as e:
        print("Failed to initialize: " + str(e))

    while True:
        main_directory = main_folder
        print("1) Open the last chapter")
        print("2) Add")
        print("3) Open")
        print("10) Close")

        choice = get_user_choice("> ")

        if choice == 1:
            print('Which subject?')
            for i, subject in enumerate(subjects, start=1):
                print(f"{i}) {subject}")

            subject_choice = get_user_choice("> ")

            if 1 <= subject_choice <= len(subjects):
                subject = subjects[subject_choice - 1]
                open_last_class(main_folder, year, subject)
            else:
                print("Invalid choice.")

        elif choice == 2:
            print("Add Menu:")
            print("1) Add a Chapter")
            print("2) Add a control")
            print("3) Add an exercise")

            action_choice = get_user_choice("> ")

            if action_choice == 1 or action_choice == 2 or action_choice == 3:
                print('Which subject?')
                for i, subject in enumerate(subjects, start=1):
                    print(f"{i}) {subject}")

                subject_choice = get_user_choice("> ")

                if 1 <= subject_choice <= len(subjects):
                    subject = subjects[subject_choice - 1]
                    if action_choice == 1:
                        add_chapter(main_directory, year, subject)
                    else:
                        chapter_folder = os.path.join(
                            main_directory, year, subject)
                        last_chapter = check_last_chapter(chapter_folder)
                        all_chapters = generate_numbers(last_chapter)

                        i = 0
                        print("Which Chapter?")
                        for chapter in all_chapters:
                            i += 1
                            chapter_name = f"{i}) Chapter{int(chapter):02d}"
                            print(chapter_name)
                        chapter_choice = get_user_choice("> ")
                        if 1 <= chapter_choice <= len(all_chapters):
                            print(all_chapters[chapter_choice - 1])
                            chapter_name = f"Chapter{
                                int(all_chapters[chapter_choice - 1]):02d}"
                            if action_choice == 2:
                                add_control(main_directory, year,
                                            subject, chapter_name)
                            elif action_choice == 3:
                                add_exercise(main_directory, year,
                                             subject, chapter_name)
                            print(os.path.join(main_directory,
                                               subject, chapter_name, year))
                        else:
                            print("Invalid choice.")
                else:
                    print("Invalid choice.")
            else:
                print("Invalid choice.")

        elif choice == 3:
            print("Open Menu:")
            print("0) Open the Course file")
            print("1) Open the year folder")
            print("2) Open a subject folder")
            print("3) Open a chapter folder")
            print("4) Open the Control file")
            print("5) Open an exercise folder")
            print("6) Open the Other folder")
            open_choice = get_user_choice("> ")

            if open_choice == 1:
                open_folder(os.path.join(main_directory, year))
            elif open_choice == 2:
                print('Which subject?')
                for i, subject in enumerate(subjects, start=1):
                    print(f"{i}) {subject}")

                subject_choice = get_user_choice("> ")

                if 1 <= subject_choice <= len(subjects):
                    subject = subjects[subject_choice - 1]
                    subject_folders = os.path.join(
                        main_directory, year, subject)
                    open_folder(subject_folders)
                else:
                    print("Invalid choice.")
            elif open_choice == 3 or open_choice == 4 or open_choice == 5 or open_choice == 6 or open_choice == 0:
                print('Which subject?')
                for i, subject in enumerate(subjects, start=1):
                    print(f"{i}) {subject}")

                subject_choice = get_user_choice("> ")

                if 1 <= subject_choice <= len(subjects):
                    subject = subjects[subject_choice - 1]
                    chapter_folder = os.path.join(
                        main_directory, year, subject)
                    last_chapter = check_last_chapter(chapter_folder)
                    all_chapters = generate_numbers(last_chapter)
                    i = 0
                    print("Which Chapter?")
                    for chapter in all_chapters:
                        i += 1
                        chapter_name = f"{i}) Chapter{int(chapter):02d}"
                        print(chapter_name)
                    chapter_choice = get_user_choice("> ")
                    if 1 <= chapter_choice <= len(all_chapters):
                        print(all_chapters[chapter_choice - 1])
                        chapter_name = f"Chapter{
                            int(all_chapters[chapter_choice - 1]):02d}"
                        if open_choice == 3:
                            open_folder(os.path.join(
                                main_directory, year, subject, chapter_name))
                        elif open_choice == 4:
                            open_folder(os.path.join(
                                main_directory, year, subject, chapter_name, "Control"))
                        elif open_choice == 5:
                            open_folder(os.path.join(
                                main_directory, year, subject, chapter_name, "Exercise"))
                        elif open_choice == 6:
                            open_folder(os.path.join(
                                main_directory, year, subject, chapter_name, "Other"))
                        elif open_choice == 0:
                            open_file(os.path.join(
                                main_directory, year, subject, chapter_name, f"{subject}_Chapter{chapter}_Course.docx"))
                    else:
                        print("Invalid choice.")
                else:
                    print("Invalid choice.")
            else:
                print("Invalid choice.")
        elif choice == 10:
            print("Closing the program")
            break
        else:
            print("Invalid choice.")
