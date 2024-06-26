# HighSchool Project

This project is designed to assist in organizing and managing educational resources for high school students. It provides an interface for users to choose between a onedrive and a Desktop computer to access and manage their study folders, including chapters, exercises, and other relevant documents.

## Key Features

-   **Computer Choice**: Allows users to choose between a onedrive and a desktop computer.
-   **Project Initialization**: Initializes the project with the necessary folders.
-   **Chapter Management**: Adds and manages chapters, quizzes, and exercises.
-   **Document Opening**: Opens the latest chapters or specific documents.

## Detailed Project Structure

The project is organized into several main folders and files for better understanding and management:

```
HighSchool Project/
├── component/ # Contains tools and scripts for resource management
│   ├── calculation_tools.py # Specific calculation tools
│   ├── check.py # Verification scripts
│   ├── creation.py # Scripts for creating new elements
│   ├── initialization.py # Script to initialize the project
│   └── open.py # Script to open documents
├── file/ # Folder for reference files
│   └── file_docx.docx # Example document
└── main.py # Main entry point of the project
```

## Quick Start

To get started with this project:

1. Clone the repository to your local machine.
2. Replace the variable `main_folder` in the `main.py` file with the path to your main folder.
3. Navigate to the project folder in your terminal.
4. Run `python main.py` to start the application.
5. Follow the on-screen instructions to navigate the application.

## Contributing

To contribute to this project:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -m 'Add some NewFeature'`).
4. Push to the branch (`git push origin feature/NewFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
