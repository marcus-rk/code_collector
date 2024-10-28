# Specify files and directories to exclude and include based on project needs
# ============================
# Configuration (modifiable)
# ============================

# ============================
# Configuration (modifiable)
# ============================

EXCLUDED_FILES = {
    # Common project artifacts and config files
    'international_names_with_rooms_1000.csv', 
    'package-lock.json', 
    'yarn.lock', 
    'Pipfile.lock', 
    'poetry.lock',
    '.gitignore', 
    '.gitattributes', 
    '.gitmodules', 
    '.DS_Store', 
    'Thumbs.db', 
    '.editorconfig', 
    '.project', 
    '.classpath', 
    'TODO', 
    'LICENSE',    # optional exclusion
    '.env', 
    '.env.local', 
    '.secrets', 
    '*.pem', 
    '*.key', 
    '.log', 
    '.swp', 
    '.bak', 
    '.orig',

    # Node.js and JavaScript development files
    'npm-debug.log', 
    '.npmrc', 
    '.eslintcache',

    # Android Studio and Jetpack Compose specific files
    'local.properties', 
    '*.iml', 
    '*.keystore',     # Optional: remove sensitive files like keystore
    'gradlew', 
    'gradlew.bat',

    # IDE and editor-specific files
    '*.sublime-workspace', 
    '*.sublime-project', 
    '.eslintrc', 
    '.prettierrc', 
    '.editorconfig',
}

EXCLUDED_DIRS = {
    # Virtual environments and dependency folders
    '.venv', 'venv', 'env',  # Python virtual environments
    'dist', 'build', 'target', 'out',  # Build artifacts
    'node_modules', 'lib', 'Lib',  # Dependency directories
    '__pycache__', '.pytest_cache', '.mypy_cache', '.ipynb_checkpoints',  # Caches and temp dirs

    # Version control and local config
    '.git', '.svn', '.hg',  # Version control metadata
    '.idea', '.vscode', '.gradle',  # IDE configurations and Gradle

    # Documentation and static site generator builds
    '_site', '.docusaurus', 'docs/_build', 

    # Android Studio and Jetpack Compose specific directories
    '.gradle',               # Android Gradle build system
    '.caches',               # Caches for IntelliJ-based IDEs (including Android Studio)
    '.android',              # Android SDK artifacts
    '.kotlin',               # Kotlin-related caches and configuration
    'build',                 # Build artifacts for Android and Java projects

    # Other IDE and system-specific caches
    '.expo', '.expo-shared', # Expo for React Native
    '.sass-cache',           # Sass cache files
    'coverage',              # Code coverage reports
    'tmp',                   # Temp files
}

INCLUDED_EXTENSIONS = ['.py', '.txt', '.js', '.html', '.htm', '.css', '.kt']

# ============================ Support for multiple languages ============================

# Python, JavaScript, HTML, CSS, Kotlin & Java