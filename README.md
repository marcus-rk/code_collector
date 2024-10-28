# Code Collector - Giving LLMs the XML They Deserve

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

## Overview

**Code Collector** is a Python script that makes wrangling your source code a breeze! It compiles files from your project directory into a single text file, all wrapped up in **XML tags** for better readability and performance for LLMs. 

- This whole idea sprouted from a frustrating moment when I realized how much **time and energy** it takes to feed language models (LLMs) like ChatGPT 4o or Claude AI Sonna with code snippets from projects that have a "great" folder structure. Sure, it’s nice to have everything organized, but good luck copying and pasting all that code from multiple folders!

- With **Code Collector**, I aimed to give LLMs the organized, structured input they need to truly shine. It’s all about making the codebase easier to analyze and process, so you can focus on the fun stuff—like coding! Learn more about this in the sections [Why XML Tags Matter](#why-xml-tags-matter-) and [Learn More About XML + AI](#learn-more-about-xml--ai-)

And here’s the best part: you can run the **Code Collector** command right from your terminal like a coding wizard! 🪄✨

## Features

- **Recursion**: Walks through the directory and all subdirectories.
- **Exclusion Filters**: Easily configure which files and directories to exclude.
- **File Output**: Generates a structured text file with the contents of the collected code.
- **Summary Report**: At the end of the process, a summary is printed that includes the total number of folders, files, lines of code, and the time taken for the collection.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#-requirements)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Exclusions](#❌-exclusions)
8. [Why XML Tags Matter](#why-xml-tags-matter-)
9. [Learn More About XML + AI](#learn-more-about-xml--ai-)
10. [Setting up `collect_code` as a Terminal Command](#setting-up-collect_code-as-a-terminal-command)
    - [Prerequisites](#prerequisites)
    - [Verifying Prerequisites](#verifying-prerequisites)
    - [macOS Setup](#macos-setup)
    - [Windows Setup](#windows-setup)
11. [Testing the Command](#testing-the-command)
12. [Troubleshooting](#troubleshooting)
13. [Future features: The Great Code Cleanup](#future-features-the-great-code-cleanup)
14. [License](#📝-license)

---

## 🛠️ Requirements

- Python 3.x installed on your system.
- Basic understanding of command line usage.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/marcus-rk/code_collector.git
   cd code-collector
   ```

2. **Navigate to the Project Directory**: Make sure you're in the directory where the `collect_code.py` file is located.

## ⚙️ Configuration

Before running the script, you may want to adjust the configuration settings to fit your needs. Open the `collect_code.py` file and find the following constants:

```python
EXCLUDED_FILES = {'international_names_with_rooms_1000.csv'}  # Files to exclude
EXCLUDED_DIRS = {'.venv', 'dist-info'}                        # Directories to exclude
INCLUDED_EXTENSIONS = {'.py', '.txt'}                         # File types to include
```

- **EXCLUDED_FILES**: Add any specific filenames that should be ignored during the collection.
- **EXCLUDED_DIRS**: Specify any directory names that should be excluded (e.g., virtual environments).
- **INCLUDED_EXTENSIONS**: List file extensions that should be included in the output.
  - *Note*: You can customize this to include other programming languages by changing the extensions. For example, use `INCLUDED_EXTENSIONS = {'.java', '.kt', '.js'}` for Java, Kotlin, or JavaScript files.

---

## Usage

1. **Run the Script**: Open your terminal and navigate to the directory where the script 'code_collect.py' is located. Use the following command:

   ```bash
   python3 collect_code.py <project_directory> <output_file>
   ```

   - Replace `<project_directory>` with the path to the directory you want to collect files from (either relative or absolute).
   - Replace `<output_file>` with the name of the output file (e.g., `codebase.txt`).

2. **Output**: The collected code will be saved to the specified output file in the same directory as the script.

## ❌ Exclusions

By default, the script excludes:

- The file `international_names_with_rooms_1000.csv`
- Any files in the `.venv` directory (used for Python virtual environments)
- Any files in directories named `dist-info` (which are created for Python package metadata)

Feel free to modify the exclusion lists as needed in 'collect_code.py'.

---


## Why XML Tags Matter 🎯

When **Code Collector** processes your project, it transforms scattered files into a structured XML format that helps LLM models:

* **Maintain Context**: 
  - Keep track of file locations
  - Understand code relationships
  - Follow project organization

* **Enhance Understanding**: 
  - Clearer project structure
  - Better code comprehension
  - More accurate analysis

* **Improve AI Responses**: 
  - More precise answers
  - Better code suggestions
  - Clearer explanations

### Learn More About XML + AI 📚

Want to dive deeper into how XML tags enhance AI comprehension? Check out these resources:

* [Anthropic's Guide to XML Tags](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
  - Learn the official best practices
  - Understand why structure matters
  - See real-world examples

* [Optimizing Claude AI Outputs](https://vectorshift.ai/blog/how-to-get-better-outputs-with-anthropic-s-claude-ai-chatbots)
  - Advanced strategies for AI interaction
  - Tips for better code analysis
  - Practical applications


---

## Setting up `wrapitup` as a Terminal Command

This guide will help you set up `wrapitup` as a system-wide command, so you can invoke its magic from any directory on your system!

### Prerequisites

- [Python 3](https://www.python.org/downloads/) (3.7 or higher recommended)
- [Git](https://git-scm.com/downloads) (for downloading the script)
- `collect_code.py` script from the [code_collector repository](https://github.com/marcus-rk/code_collector.git)

#### Verifying Prerequisites

Make sure your installations are working by running:
```bash
python3 --version
git --version
```

### macOS Setup

#### 1. Initial Setup (One Command)

```bash
# Create bin directory, add to PATH, and apply changes
mkdir -p ~/bin && \
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc && \
echo 'alias wrapitup="python3 ~/bin/collect_code.py"' >> ~/.zshrc && \
source ~/.zshrc
```

#### 2. Install Script

```bash
# Clone repo, move script, and make executable
git clone https://github.com/marcus-rk/code_collector.git && \
mv code_collector/collect_code.py ~/bin/ && \
chmod +x ~/bin/collect_code.py && \
rm -rf code_collector
```

That's it! You can now use `wrapitup` from anywhere.

### Windows Setup

#### 1. Initial Setup (PowerShell as Administrator)

```powershell
# Create Scripts directory and add to PATH
mkdir $HOME\Scripts
[Environment]::SetEnvironmentVariable(
    "Path",
    [Environment]::GetEnvironmentVariable("Path", "User") + ";%USERPROFILE%\Scripts",
    "User"
)
```

#### 2. Install Script and Create Batch File

```powershell
# Clone repo, move script, create batch file
git clone https://github.com/marcus-rk/code_collector.git
move code_collector\collect_code.py $HOME\Scripts\
echo @echo off > $HOME\Scripts\collect_code.bat
echo python "%USERPROFILE%\Scripts\collect_code.py" %* >> $HOME\Scripts\collect_code.bat
Remove-Item -Recurse -Force code_collector
```

Restart your terminal for changes to take effect.

## Testing the Command

The command works the same way on both operating systems:

```bash
collect_code  
```

Example:
```bash
collect_code ../MyProject codebase.txt
```

### Troubleshooting

If the command isn't recognized after installation:
1. Make sure you've restarted your terminal
2. Verify Python is in your system PATH (you can add it during [Python installation](https://docs.python.org/3/using/windows.html#installation-steps))
3. Check if the script has proper permissions (macOS)
4. Ensure the batch file was created correctly (Windows)

---

### Future features: **The Great Code Cleanup**

- ✨ **Auto-Delete Feature** – After you’re done with the output file, it’ll vanish like magic, leaving your workspace spotless. Access your insights instantly, minus the digital clutter!

## 📝 License

This project is licensed under the MIT License. 

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
