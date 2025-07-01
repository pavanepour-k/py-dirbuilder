from py_dirbuilder.cli.menu import show_main_menu
from py_dirbuilder.cli.input_ui import select_structure_file, select_target_dir, confirm
from py_dirbuilder.builder.templates import select_templates
from py_dirbuilder.builder.builder import build_dir
from py_dirbuilder.parser.autodetect import AutoDetectParser
from py_dirbuilder.display.tree import print_tree

def main():
    selected_templates = []
    while True:
        choice = show_main_menu()
        if choice == 1:
            structure_file = select_structure_file()
            if not structure_file:
                continue
            with open(structure_file, encoding="utf-8") as f:
                structure_text = f.read()
            tree = AutoDetectParser().parse(structure_text)
            print("\nStructure Preview:")
            print_tree(tree)
            if not confirm("Do you want to create the structure as shown? (y/n): "):
                continue
            target_dir = select_target_dir()
            if not target_dir:
                continue
            build_dir(tree, target_dir, templates=selected_templates)
            print("Directories and files have been created successfully!")
        elif choice == 2:
            selected_templates = select_templates()
            if selected_templates:
                print("Selected templates will be applied.")
        elif choice == 3:
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()

