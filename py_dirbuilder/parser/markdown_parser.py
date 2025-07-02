from py_dirbuilder.models import Node
from py_dirbuilder.parser.base import BaseParser
from py_dirbuilder.exceptions import ParseError
from typing import List

class MarkdownParser(BaseParser):
    """Parses Markdown lists (ul/li) into a Node tree"""

    def parse(self, source: str) -> Node:
        """
        Example input:
        - root
            - dir1
                - file1.txt
            - file2.txt
        """
        lines = source.splitlines()
        if not lines:
            raise ParseError("Input data is empty.")

        # Process the first line as the root
        root_name = lines[0].lstrip('-* ').strip()
        root = Node(name=root_name, is_file='.' in root_name)
        stack: List[(int, Node)] = [(0, root)]

        for line in lines[1:]:
            if not line.strip():
                continue
            indent = len(line) - len(line.lstrip())
            name = line.lstrip('-* ').strip()
            is_file = '.' in name
            node = Node(name=name, is_file=is_file)

            while stack and indent <= stack[-1][0]:
                stack.pop()
            if stack:
                stack[-1][1].add_child(node)
            stack.append((indent, node))
        return root
