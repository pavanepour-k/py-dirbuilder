import os

# ANSI Color Code Definition
ANSI_CODES = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
}

def supports_color() -> bool:
    """Determine if the current terminal supports ANSI color code

    Returns:
        bool: True with color support
    """
    if os.name == 'nt':
        # Windows: Windows Terminal
        return 'ANSICON' in os.environ or 'WT_SESSION' in os.environ
    else:
        return hasattr(os.sys.stdout, "isatty") and os.sys.stdout.isatty()

def colorize(text: str, color: str, bold: bool = False) -> str:
    """Apply ANSI color code to text

    Args:
        text (str): Text to output
        color (str): Color name ('red', 'green', ...)
        bold (bool): Check Bold 

    Returns:
        str: Colored text (return the original if the color is not supported)
    """
    if not supports_color() or color not in ANSI_CODES:
        return text
    prefix = ANSI_CODES[color]
    if bold:
        prefix = ANSI_CODES['bold'] + prefix
    return f"{prefix}{text}{ANSI_CODES['reset']}"