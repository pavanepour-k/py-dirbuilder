# py-dirbuilder

![Python](https://img.shields.io/badge/Python-3.8--3.13-blue)
[![CI](https://github.com/pavanepour-k/py-dirbuilder/actions/workflows/ci.yml/badge.svg)](https://github.com/pavanepour-k/py-dirbuilder/actions)

A Python CLI tool to create directory and file structures from text-based representations.  
**Supports Python 3.8–3.13 only.**  
Compatible with Windows, Linux, and macOS.

---

## Features

- **Flexible Parsing**: Supports both ASCII tree-style and Markdown-style folder/file structures
- **Automated Generation**: Creates directories and empty files as described in the input
- **Interactive CLI**: Easy-to-use menu for structure selection, target directory, and template options
- **Template System**: Extensible support for files like `README.md`, `.gitignore`, etc.
- **Continuous Integration**: Thoroughly tested via GitHub Actions and pytest

---

## Supported Python Versions

| Supported                           | Not Supported               |
| ------------------------------------ | -------------------------- |
| 3.8, 3.9, 3.10, 3.11, 3.12, 3.13    | 3.7 and below, 3.14+       |

---

## Installation

1. **Clone the repository**
    ```sh
    git clone https://github.com/pavanepour-k/py-dirbuilder.git
    cd py-dirbuilder
    ```
2. **(Optional) Create and activate a virtual environment**
    ```sh
    python -m venv .venv
    # Linux/macOS
    source .venv/bin/activate
    # Windows
    .venv\Scripts\activate
    ```
3. **Install in editable/development mode**
    ```sh
    pip install -e .
    ```

---

## Usage

### Launch the CLI

```sh
python -m py_dirbuilder.cli.main
```

You will see a menu with options:

- **Generate directories/files from a structure file**
- **Configure template files to be added**
- **Exit**

---

## Example Input File

**ASCII tree-style**










---

## Contributing

Pull requests and issues are welcome!

- Please ensure all tests pass before submitting a PR.
- See `CONTRIBUTING.md` for guidelines (coming soon).

---

## License

[MIT License](LICENSE)