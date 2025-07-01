import os
from builder.templates import add_templates

def test_add_templates(tmp_path):
    # builtin_templates에 'README.md' 파일이 반드시 있어야 함
    from builder.templates import TEMPLATE_DIR
    open(os.path.join(TEMPLATE_DIR, "README.md"), "w").write("# Sample")

    add_templates(str(tmp_path), ["README.md"])
    assert (tmp_path / "README.md").exists()