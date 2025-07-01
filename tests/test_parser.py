import pytest
from parser.tree_parser import TreeParser
from parser.markdown_parser import MarkdownParser
from parser.autodetect import AutoDetectParser

def test_tree_parser():
    source = """root
    ├── dir1
    │   └── file1.txt
    └── file2.txt
    """
    parser = TreeParser()
    tree = parser.parse(source)
    assert tree.name == 'root'
    assert len(tree.children) == 2
    assert tree.children[0].name == 'dir1'
    assert tree.children[1].name == 'file2.txt'
    assert tree.children[0].children[0].name == 'file1.txt'

def test_markdown_parser():
    source = """- root
    - dir1
        - file1.txt
    - file2.txt
    """
    parser = MarkdownParser()
    tree = parser.parse(source)
    assert tree.name == 'root'
    assert len(tree.children) == 2
    assert tree.children[0].name == 'dir1'
    assert tree.children[1].name == 'file2.txt'

def test_autodetect_parser_tree():
    source = """root
    └── file.txt
    """
    parser = AutoDetectParser()
    tree = parser.parse(source)
    assert tree.name == 'root'
    assert tree.children[0].name == 'file.txt'

def test_autodetect_parser_markdown():
    source = """- root
    - file.txt
    """
    parser = AutoDetectParser()
    tree = parser.parse(source)
    assert tree.name == 'root'
    assert tree.children[0].name == 'file.txt'