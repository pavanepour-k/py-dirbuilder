from pathlib import Path
from typing import Optional

def is_valid_path(path_str: str) -> bool:
    """Check path string is valid

    Args:
        path_str (str): Path string to check

    Returns:
        bool: If it's a valid path, it's True, or False
    """
    try:
        Path(path_str)
        return True
    except Exception:
        return False

def to_absolute(path_str: str, base: Optional[str] = None) -> Path:
    """Converting Path to Absolute Path

    Args:
        path_str(str): input path
        base (Optional[str]): base directory (if not present)

    Returns:
        Path: Absolute Path Object
    """
    base_path = Path(base) if base else Path.cwd()
    return (base_path / path_str).resolve()

def is_subpath(parent: Path, child: Path) -> bool:
    """Check if the child path is subordinate to the parent path

    Args:
        parent (Path): Parental Path
        child (Path): Paths to be examined

    Returns:
        bool: If it's a subpath, it's True, or False
    """
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False