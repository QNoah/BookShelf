from Book import Book
from Library import Library

library = Library()
# book = Book("title", "category", "author", 200, 0) // to create a new book

def main_menu():
    print("1. Add Book")
    print("2. Edit Book")
    print("3. Remove Book")
    print("4. Credits")
    print()
    choice = input("")
    
    if choice == "1":
        library.add_book()

main_menu()