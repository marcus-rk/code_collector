# Code Collector

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)



## Overview

**Code Collector** is a Python script created to simplify the process of compiling source code files from a specified project directory into a single text file formatted with XML tags. The primary goal of this project is to enhance the ability of language models (LLMs) like ChatGPT and Claude AI to understand and process an entire codebase effectively. By organizing the code into a structured format, it becomes easier to analyze, document, and share snippets, while also allowing for the exclusion of unnecessary files.

## Features

- **Recursion**: Walks through the directory and all subdirectories.
- **Exclusion Filters**: Easily configure which files and directories to exclude.
- **File Output**: Generates a structured text file with the contents of the collected code.
- **Summary Report**: At the end of the process, a summary is printed that includes the total number of folders, files, lines of code, and the time taken for the collection.

## Requirements

- Python 3.x installed on your system.
- Basic understanding of command line usage.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/marcus-rk/code_collector.git
   cd code-collector
   ```

2. **Navigate to the Project Directory**: Make sure you're in the directory where the `collect_code.py` file is located.

## Configuration

Before running the script, you may want to adjust the configuration settings to fit your needs. Open the `collect_code.py` file and find the following constants:

```python
EXCLUDED_FILES = {'international_names_with_rooms_1000.csv'}  # Files to exclude
EXCLUDED_DIRS = {'.venv', 'dist-info'}                        # Directories to exclude
INCLUDED_EXTENSIONS = {'.py', '.txt'}                         # File types to include
```

- **EXCLUDED_FILES**: Add any specific filenames that should be ignored during the collection.
- **EXCLUDED_DIRS**: Specify any directory names that should be excluded (e.g., virtual environments).
- **INCLUDED_EXTENSIONS**: List file extensions that should be included in the output.

## Usage

1. **Run the Script**: Open your terminal and navigate to the directory where the script 'code_collect.py' is located. Use the following command:

   ```bash
   python3 collect_code.py <project_directory> <output_file>
   ```

   - Replace `<project_directory>` with the path to the directory you want to collect files from (either relative or absolute).
   - Replace `<output_file>` with the name of the output file (e.g., `codebase.txt`).

2. **Output**: The collected code will be saved to the specified output file in the same directory as the script.

## Exclusions

By default, the script excludes:

- The file `international_names_with_rooms_1000.csv`
- Any files in the `.venv` directory (used for Python virtual environments)
- Any files in directories named `dist-info` (which are created for Python package metadata)

Feel free to modify the exclusion lists as needed in 'collect_code.py'.

---

## Using `collect_code` as a Custom Terminal Command

### Method 1: Using an Alias

1.  **Open Terminal**:
    
    *   Launch the Terminal application.
2.  **Open Your Shell Configuration File**:
    
    *   Since you’re likely using `zsh` by default on macOS Sonoma, open your `.zshrc` file:
    
    ```bash
    nano ~/.zshrc
    ```
    
3.  **Add the Alias**:
    
    *   At the bottom of the file, add the alias. Make sure to replace `/path/to/your/script` with the full path to your `collect_code.py` script. For example:
    
    ```bash
    alias collect_code='python3 /Users/marcus_rk/Softwarearkitektur/Hotel_Kong_Arthur/code_collector/collect_code.py'
    ```
    
4.  **Save and Exit**:
    
    *   Press `CTRL + X`, then `Y`, and finally `Enter` to save and exit.
5.  **Apply Changes**:
    
    *   Load your updated `.zshrc` into the current terminal session:
    
    ```bash
    source ~/.zshrc
    ```
    
6.  **Using the Alias**:
    
    *   You can now run the command from anywhere in your terminal:
    
    ```bash
    collect_code <project_directory> <output_file>
    ```
    
    Example:
    
    ```bash
    collect_code ../ReservationService codebase.txt
    ```

### Method 2: Creating a Shell Script

1.  **Create a Directory for Scripts (Optional)**:
    
    *   If you don’t already have a directory for scripts, you can create one. A common practice is to use `~/bin`.
    
    ```bash
    mkdir -p ~/bin
    ```
    
2.  **Create the Shell Script**:
    
    *   Navigate to the `~/bin` directory:
    
    ```bash
    cd ~/bin
    ```
    
    *   Create a new shell script:
    
    ```bash
    nano collect_code
    ```
    
3.  **Write the Shell Script**:
    
    *   Add the following lines to the `collect_code` file. Remember to replace the path accordingly:
    
    ```bash
    #!/bin/bash
    python3 /Users/marcus_rk/Softwarearkitektur/Hotel_Kong_Arthur/code_collector/collect_code.py "$@"
    ```
    
4.  **Save and Exit**:
    
    *   Save your changes (CTRL + X, Y, Enter).
5.  **Make the Script Executable**:
    
    *   Change the permissions to make the script executable:
    
    ```bash
    chmod +x collect_code
    ```
    
6.  **Add `~/bin` to Your PATH (if not already)**:
    
    *   Open your `.zshrc` file again:
    
    ```bash
    nano ~/.zshrc
    ```
    
    *   Add the following line if `~/bin` isn’t already in your PATH:
    
    ```bash
    export PATH="$HOME/bin:$PATH"
    ```
    
7.  **Apply Changes**:
    
    *   Load your updated `.zshrc`:
    
    ```bash
    source ~/.zshrc
    ```
    
8.  **Using the Shell Script**:
    
    *   Now you can execute the command from any terminal session like this:
    
    ```bash
    collect_code <project_directory> <output_file>
    ```
    
    Example:
    
    ```bash
    collect_code ../ReservationService codebase.txt
    ```

### Testing the Command

After you set up either the alias or the shell script, test it to ensure it works correctly:

1.  Open a new terminal session.
    
2.  Run the command:
    
    ```bash
    collect_code ../ReservationService codebase.txt
    ```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.