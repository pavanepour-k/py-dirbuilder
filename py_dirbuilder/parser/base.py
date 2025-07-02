from py_dirbuilder.models import Node
from abc import ABC, abstractmethod

class BaseParser(ABC):
    """Abstract parser class that converts tree input into a Node tree"""

    @abstractmethod
    def parse(self, source: str) -> Node:
        """Converts the input source into a Node tree

        Args:
            source (str): Input text

        Returns:
            Node: Root node of the tree

        Raises:
            ParseError: When parsing fails
        """
        pass