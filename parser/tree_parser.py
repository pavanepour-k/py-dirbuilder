from .base import Node, BaseParser
from exceptions import ParseError
from typing import List

class TreeParser(BaseParser):
    """Converts a text-based tree format into a Node tree"""

    def parse(self, source: str) -> Node:
        """
        Example input:
        root
        ├── dir1
        │   └── file1.txt
        └── file2.txt
        """
        lines = source.splitlines()
        if not lines:
            raise ParseError("Input data is empty.")

        root_name = lines[0].strip()
        root = Node(name=root_name, is_file=False)
        stack: List[(int, Node)] = [(0, root)]

        for line in lines[1:]:
            stripped = line.lstrip()
            if not stripped:
                continue
            indent = len(line) - len(stripped)
            is_file = '.' in stripped  # Simple check for file
            name = stripped.lstrip('├─│ ').rstrip()
            node = Node(name=name, is_file=is_file)

            # Find position in hierarchy
            while stack and indent <= stack[-1][0]:
                stack.pop()
            if stack:
                stack[-1][1].add_child(node)
            stack.append((indent, node))

        return root
