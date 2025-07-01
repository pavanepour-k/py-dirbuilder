import os
import shutil
from builder.builder import build_dir
from parser.tree_parser import Node

def test_build_dir(tmp_path):
    root = Node(name="testroot", is_file=False, children=[
        Node(name="src", is_file=False, children=[
            Node(name="main.py", is_file=True)
        ]),
        Node(name="README.md", is_file=True)
    ])
    target = tmp_path / "out"
    build_dir(root, str(target))

    assert (target / "testroot").exists()
    assert (target / "testroot" / "src").exists()
    assert (target / "testroot" / "src" / "main.py").exists()
    assert (target / "testroot" / "README.md").exists()