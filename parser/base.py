from dataclasses import dataclass, field
from typing import List, Optional
from abc import ABC, abstractmethod

@dataclass
class Node:
    """Node Data Model in Directory Tree

    Attributes:
        name (str): File or directory name
        is_file (bool): File status (True: File, False: Dir)
        children (List['Node']): Sub-Node List
    """
    name: str
    is_file: bool = False
    children: List['Node'] = field(default_factory=list)

    def add_child(self, node: 'Node') -> None:
        """Add Subnode"""
        self.children.append(node)