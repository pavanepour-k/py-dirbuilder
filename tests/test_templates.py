import os
from py_dirbuilder.builder.templates import add_templates

def test_add_templates(tmp_path):
    from py_dirbuilder.builder.templates import TEMPLATE_DIR
    open(os.path.join(TEMPLATE_DIR, "README.md"), "w").write("# Sample")

    add_templates(str(tmp_path), ["README.md"])
    assert (tmp_path / "README.md").exists()