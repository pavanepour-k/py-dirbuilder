from typing import List
from dataclasses import dataclass, field

@dataclass
class Node:
    name: str
    is_file: bool = False
    children: List['Node'] = field(default_factory=list)

class TreeParser:
    def parse(self, source: str) -> Node:
        lines = [line.rstrip() for line in source.splitlines() if line.strip()]
        stack = []
        root = None

        for line in lines:
            prefix = line.split('├', 1)[0].split('└', 1)[0]
            indent = 0
            i = 0
            while i < len(prefix):
                if prefix[i] == '│':
                    indent += 1
                    i += 1
                elif prefix[i:i+4] == '    ':
                    indent += 1
                    i += 4
                else:
                    i += 1

            name = line
            for token in ['├── ', '└── ', '│   ', '    ']:
                name = name.replace(token, '')
            name = name.strip()
            is_file = '.' in name

            node = Node(name=name, is_file=is_file)

            if indent == 0:
                root = node
                stack = [root]
            else:
                stack = stack[:indent]
                parent = stack[-1]
                parent.children.append(node)
                stack.append(node)

        return root
