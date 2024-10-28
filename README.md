# Code Collector

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.