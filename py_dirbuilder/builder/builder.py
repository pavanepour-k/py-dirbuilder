import os

def build_dir(node, target_dir, templates=None):
    # node: Root of the tree (Node), target_dir: Directory creation path
    # templates: List of template files
    _create(node, target_dir)
    if templates:
        from .templates import add_templates
        add_templates(target_dir, templates)

def _create(node, parent_path):
    path = os.path.join(parent_path, node.name)
    if node.is_file:
        open(path, "w").close()
    else:
        os.makedirs(path, exist_ok=True)
        for child in node.children:
            _create(child, path)
