def print_tree(node, prefix=""):
    print(prefix + node.name)
    children = node.children
    for idx, child in enumerate(children):
        last = idx == len(children) - 1
        branch = "└── " if last else "├── "
        sub_prefix = prefix + ("    " if last else "│   ")
        print(branch, end="")
        print_tree(child, prefix=sub_prefix)