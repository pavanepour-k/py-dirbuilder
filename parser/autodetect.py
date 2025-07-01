from .tree_parser import TreeParser
from .markdown_parser import MarkdownParser
from .base import Node, BaseParser
from exceptions import ParseError

class AutoDetectParser(BaseParser):
    """Automatically detects the input string format and uses the appropriate parser"""

    def parse(self, source: str) -> Node:
        # Simple detection: if starts with '-' or '*', it's Markdown; if contains '├', etc., it's a tree
        if not source.strip():
            raise ParseError("Input data is empty.")

        if any(line.lstrip().startswith(('-', '*')) for line in source.splitlines()):
            return MarkdownParser().parse(source)
        if any('├' in line or '└' in line for line in source.splitlines()):
            return TreeParser().parse(source)
        raise ParseError("Unsupported input format.")