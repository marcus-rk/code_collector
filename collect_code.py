import os
import sys
import time

# ============================
# Configuration (modifiable)
# ============================
EXCLUDED_FILES = {'international_names_with_rooms_1000.csv'} 
EXCLUDED_DIRS = {'.venv', 'dist-info'} 
INCLUDED_EXTENSIONS = {'.py', '.txt'} 

# ============================
# Utility Functions
# ============================

def is_excluded(file_name, dir_path):
    """Check if a file or directory should be excluded based on predefined criteria."""
    if file_name in EXCLUDED_FILES:
        return True
    if any(excluded_dir in dir_path for excluded_dir in EXCLUDED_DIRS):
        return True
    return False

def print_summary(summary, output_file, base_dir):
    """Print the summary of the collection in a readable format."""
    base_name = os.path.basename(base_dir)  # Get the last component of the base_dir

    print(f'Codebase {base_name} collected into {output_file}')
    print(f'Total folders: {summary["folders"]}')
    print(f'Total files: {summary["files"]}')
    print(f'Total lines of code: {summary["lines"]}')
    print(f'Time taken: {summary["time"]:.2f} seconds')

# ============================
# Main Code Collection Logic
# ============================

def collect_code(base_dir, output_file):
    """Collect code from the specified base directory and write to an output file."""
    
    # Initialize a summary dictionary
    summary = {'folders': 0, 'files': 0, 'lines': 0, 'time': 0}

    start_time = time.time()  # Start timing

    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Walk through the directory
        for root, dirs, files in os.walk(base_dir):
            # Count only the immediate folders in the base_dir
            if root == base_dir:
                summary['folders'] += len(dirs)  # Count only immediate subdirectories

            for filename in files:
                if is_excluded(filename, root):
                    continue  # Skip excluded files and directories

                # Include files with specified extensions
                if any(filename.endswith(ext) for ext in INCLUDED_EXTENSIONS):
                    file_path = os.path.join(root, filename)
                    outfile.write(f'<file path="{file_path}">\n')  # Open tag with file path

                    with open(file_path, 'r', encoding='utf-8') as infile:
                        file_content = infile.read()
                        outfile.write(file_content)  # Write file content
                        summary['lines'] += file_content.count('\n') + 1  # Count lines

                    outfile.write(f'\n</file>\n\n')  # Close tag with separation
                    summary['files'] += 1  # Increment file count

    end_time = time.time()  # End timing
    summary['time'] = end_time - start_time  # Calculate elapsed time

    # Print summary of the collection
    print_summary(summary, output_file, base_dir)

# ============================
# Main Entry Point
# ============================

if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 collect_code.py <project_directory> [<output_file>]")
        sys.exit(1)

    project_directory = sys.argv[1].strip()  # Get the directory from command-line argument
    output_filename = sys.argv[2].strip() if len(sys.argv) == 3 else 'codebase.txt'  # Use the second argument or default to 'codebase.txt'

    # Call the function to collect code
    collect_code(project_directory, output_filename)
