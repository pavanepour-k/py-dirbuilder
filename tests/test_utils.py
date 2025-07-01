from pathlib import Path
from utils.path import is_valid_path, to_absolute, is_subpath
from utils.file import ensure_dir, file_exists

def test_is_valid_path():
    assert is_valid_path('abc')
    assert is_valid_path('/tmp')
    assert is_valid_path('./relative/path')

def test_to_absolute():
    abs_path = to_absolute('tmp')
    assert abs_path.is_absolute()

def test_is_subpath():
    p = Path('/a/b')
    c = Path('/a/b/c/d')
    assert is_subpath(p, c)
    assert not is_subpath(c, p)

def test_ensure_dir(tmp_path):
    d = tmp_path / 'new_dir'
    ensure_dir(d)
    assert d.exists() and d.is_dir()

def test_file_exists(tmp_path):
    f = tmp_path / 'file.txt'
    f.write_text('hello')
    assert file_exists(f)
