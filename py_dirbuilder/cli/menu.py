def show_main_menu():
    print("\npy-dirbuilder")
    print("-" * 30)
    print("1. Structure File → Directory/File Creation")
    print("2. Additional Options (Template/Default File")
    print("3. Shutdown")
    while True:
        choice = input("Please select a number: ").strip()
        if choice in {'1', '2', '3'}:
            return int(choice)
        print("Enter a number between 1 and 3")