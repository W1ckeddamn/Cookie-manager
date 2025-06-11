# Cookie Manager

Cookie Manager is a graphical Python application that allows users to manage cookie profiles. Users can add profiles with a name and an optional description, which are saved in a designated folder. The application also provides functionality to open a web browser for user interaction.

## Features

- Add and remove cookie profiles
- Save cookies in individual folders
- User-friendly interface built with Tkinter
- Open a web browser for easy access

## Project Structure

```
cookie-manager
├── src
│   ├── main.py                # Entry point of the application
│   ├── managers
│   │   └── cookie_manager.py   # Logic for managing cookie profiles
│   ├── utils
│   │   └── file_handler.py      # Utility functions for file operations
│   └── ui
│       ├── dialogs.py          # Dialogs for user input
│       └── main_window.py      # Main user interface setup
├── profiles                     # Directory for storing profile folders
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd cookie-manager
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## License

This project is licensed under the MIT License.