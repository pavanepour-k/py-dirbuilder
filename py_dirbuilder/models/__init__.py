from dataclasses import dataclass, field
from typing import List

@dataclass
class Node:
    """Represents a directory tree node."""
    name: str
    is_file: bool = False
    children: List['Node'] = field(default_factory=list)

    def add_child(self, node: 'Node') -> None:
        """Add a child node."""
        self.children.append(node)