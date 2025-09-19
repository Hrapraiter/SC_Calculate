from pathlib import Path

def get_files_this_directory(directory='.'):
    path = Path(directory)
    
    files = []
    for item in path.iterdir():
        if item.is_file():
            files.append(f"{directory}{item.name}")
    
    return files
