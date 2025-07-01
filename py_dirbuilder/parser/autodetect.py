from py_dirbuilder.parser.tree_parser import TreeParser
from py_dirbuilder.parser.markdown_parser import MarkdownParser

class AutoDetectParser:
    def parse(self, source: str):
        if any(x in source for x in ('├', '└')):
            return TreeParser().parse(source)
        if any(x in source for x in ('-', '*')):
            return MarkdownParser().parse(source)
        raise ValueError("Unsupported input format.")
