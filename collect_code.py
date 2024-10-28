import os
import sys
import time
import subprocess

# ============================
# Configuration (modifiable)
# ============================


EXCLUDED_FILES = {'international_names_with_rooms_1000.csv'} 
EXCLUDED_DIRS = {'.venv', 'dist-info'} 
INCLUDED_EXTENSIONS = ['.py', '.txt']

# ============================
# Utility Functions
# ============================

def is_excluded_file(file_name, dir_path):
    """Check if a file or directory should be excluded based on predefined criteria."""
    full_path = os.path.join(dir_path, file_name)  # Construct the full path

    # Check if the current path starts with any excluded directory
    for excluded_dir in EXCLUDED_DIRS:
        excluded_dir_path = os.path.join(dir_path, excluded_dir)
        if full_path.startswith(excluded_dir_path):
            return True

    return file_name in EXCLUDED_FILES

def is_included_extension(file_name):
    """Check if a file has an extension that should be included."""
    return any(file_name.endswith(ext) for ext in INCLUDED_EXTENSIONS)

def write_file_content(outfile, file_path):
    """Read a file's content and write it to the output file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
            outfile.write(content)
            return content.count('\n') + 1  # Count lines
    except Exception as e:
        print(f'Could not read {file_path}: {e}')  # Print a message if reading fails
        return 0  # Return 0 lines if the file cannot be read

def print_summary(summary, output_file, base_dir):
    """Print the summary of the collection in a readable format and open the output file."""
    base_name = os.path.basename(os.path.abspath(base_dir))  # Get only the last component of the full path
    output_file_path = os.path.abspath(output_file)  # Get the absolute path of the output file

    print('═' * 50)
    print(f'Codebase "{base_name}" has been transformed into "{output_file}". You are welcome buddy.')
    print(f'Total folders: {summary["folders"]}. You must really enjoy organizing things, huh?')
    print(f'Files collected: {summary["files"]}. That is *file-tastic*')
    print(f'Total lines: {summary["lines"]}. Yikes!')
    print(f'Time taken? Just {summary["time"]:.2f} seconds - light work!')
    print(f'My masterpiece can be found here: {output_file_path}. Surely there is no mistakes, right?')
    print('═' * 50)

    open_output_file(output_file_path)

# ============================
# Main Code Collection Logic
# ============================

def process_file(outfile, filename, root, summary):
    """Check if the file is valid, then write its content to the output file."""
    if is_included_extension(filename) and not is_excluded_file(filename, root):
        file_path = os.path.join(root, filename)
        outfile.write(f'<file path="{file_path}">\n')  # Open tag with file path
        summary['lines'] += write_file_content(outfile, file_path)  # Add lines from the file
        outfile.write(f'\n</file path="{file_path}">\n\n')  # Close tag with separation
        summary['files'] += 1  # Increment file count

def collect_code(base_dir, output_file):
    """Collect code from the specified base directory and write to an output file."""
    summary = {'folders': 0, 'files': 0, 'lines': 0, 'time': 0}
    start_time = time.time()

    # Open the output file and start writing the codebase
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(base_dir):
            # Remove excluded directories from dirs list to prevent walking into them
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
            
            if root == base_dir:
                summary['folders'] += len(dirs)  # Root directory is not counted. Increment for subdirectories.

            # Process each file in the current directory
            for filename in files:
                process_file(outfile, filename, root, summary)

    # Calculate the time taken and print summary
    summary['time'] = time.time() - start_time
    print_summary(summary, output_file, base_dir)

def open_output_file(file_path):
    """Open the output file using the default application and delete it after closing."""
    try:
        # Start the appropriate process to open the file based on the operating system
        if sys.platform == "win32":
            process = subprocess.Popen(['start', '', file_path], shell=True)
        elif sys.platform == "darwin":
            process = subprocess.Popen(['open', file_path])
        else:
            process = subprocess.Popen(['xdg-open', file_path])

        # Wait for the file to be closed before proceeding
        time.sleep(0.5) # temp solution
        process.wait()

        # This code only runs after the user closes the file/application
        os.remove(file_path)
        print(f"The file '{file_path}' has been deleted after closing.")
    except Exception as e:
        print(f"Could not open or delete the output file: {e}")

# ============================
# Main Entry Point
# ============================

if __name__ == "__main__":
    # Check if the project directory is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python3 collect_code.py <project_directory> [<output_file>]")
        sys.exit(1)
    
    # Get the project directory and output filename from the command line arguments
    project_directory = sys.argv[1].strip()
    output_filename = sys.argv[2].strip() if len(sys.argv) == 3 else 'codebase.txt' # Default output file name is codebase.txt

    # Collect code from the project directory and write to the output file
    collect_code(project_directory, output_filename)
