import pytest
from parser.base import Node

def test_node_add_child():
    parent = Node(name='root')
    child = Node(name='file.txt', is_file=True)
    parent.add_child(child)
    assert len(parent.children) == 1
    assert parent.children[0].name == 'file.txt'
    assert parent.children[0].is_file is True