# Automated File Organizer 🗂️

**INTERNID:** CITS8323

A fast, lightweight, and automated Python script designed to instantly tidy up messy directories (like your Downloads or Desktop folder). It scans the specified directory and automatically moves files into categorized subfolders based on their file extensions.

## Features

* **Zero Dependencies:** Built entirely with Python's standard library (`pathlib` and `shutil`). No need to run `pip install`.
* **Smart Categorization:** Automatically sorts files into predefined folders like Images, Documents, Audio, Videos, and Code.
* **Fallback Folder:** Any unrecognized or custom file types are safely moved into an "Others" folder.
* **Overwrite Protection:** Checks if a file with the exact same name already exists in the destination folder and skips it to prevent accidental data loss.

## Prerequisites

* Python 3.6 or newer installed on your system.

## Usage

1. **Clone or Download** this repository/script to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the script.
4. Run the script using Python:
   ```bash
   python organise.py
   
