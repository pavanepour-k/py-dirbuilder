"""
Python 3.8+ support
Define Project Public Custom Exception Classes
"""

class PyDirBuilderError(Exception):
    """Default exception class for py_dirbuilder"""
    pass

class ParseError(PyDirBuilderError):
    """Input format or parsing error"""
    pass

class FileAccessError(PyDirBuilderError):
    """File/directory inaccessible exceptions"""
    pass

class InvalidCommandError(PyDirBuilderError):
    """Invalid CLI Command Exception"""
    pass
