from pathlib import Path
from typing import List

def list_files_recursive(dir_path: Path) -> List[Path]:
    """Return all files/folder lists under the directory recursively

    Args:
        dir_path (Path): Directory path to navigate

    Returns:
        List[Path]: Path list of all sub files/folders
    """
    return list(dir_path.rglob('*'))

def ensure_dir(path: Path) -> None:
    """Create directory if it does not exist (do nothing if it already exists)

    Args:
        path (Path): Directory path to create
    """
    path.mkdir(parents=True, exist_ok=True)

def file_exists(path: Path) -> bool:
    """Verify that files/directories exist

    Args:
        path (Path): Paths to be examined

    Returns:
        bool: If it exists, it's true, or it's false
    """
    return path.exists()