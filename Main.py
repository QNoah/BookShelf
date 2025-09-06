import os
import shutil
from Book import Book
from Library import Library

library = Library()
# book = Book("title", "category", "author", 200, 0) // to create a new book

def main_menu():
    os.system('clear')
    print("Menu")
    print("-" * shutil.get_terminal_size().columns)
    print("1. Show Books")
    print("2. Add Book")
    print("3. Edit Book")
    print("4. Remove Book")
    print("5. Credits")
    print()
    choice = input("")
    
    if choice == "1": 
        library.show_all_books()
    elif choice == "2":
        library.add_book()
    elif choice == "3":
        ...
    elif choice == "4":
        library.remove_book()
    else:
        input("Thats not a valid choice! [Enter]")
    main_menu()

main_menu()