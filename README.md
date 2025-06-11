# Cookie Manager

A Python application for managing browser cookies with profile support.

## Download

### Option 1: Download Executable
1. Go to [Releases](https://github.com/W1ckeddamn/cookie-manager/releases)
2. Download the latest `cookie-manager.exe` from the Assets section
3. Run the executable directly - no installation needed

### Option 2: From Source Code
```bash
git clone https://github.com/W1ckeddamn/cookie-manager.git
cd cookie-manager
pip install -r requirements.txt
python main.py
```

## Features

- Create and manage multiple browser profiles
- Save cookies and browser data separately for each profile
- Open Edge browser with selected profile
- Modern and user-friendly interface
- Anti-detection mechanisms for browser automation

## Requirements

- Python 3.8+
- Microsoft Edge browser
- Required Python packages:
  - selenium
  - webdriver-manager
  - tkinter (usually comes with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/W1ckeddamn/cookie-manager.git
cd cookie-manager
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

### Creating a Profile
1. Click "ADD" button
2. Enter profile name and description
3. Click "OK" to create the profile

### Opening Browser
1. Select a profile from the list
2. Click "BROWSER" to open Edge with the selected profile

## Project Structure

```
cookie-manager/
├── assets/
│   └── icon.png
├── src/
│   ├── managers/
│   │   └── cookie_manager.py
│   ├── ui/
│   │   ├── main_window.py
│   │   └── dialogs.py
│   └── utils/
│       └── file_handler.py
├── main.py
└── README.md
```
