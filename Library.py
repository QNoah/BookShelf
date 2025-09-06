import os
from Book import Book

class Library:
    def __init__(self):
        self.books = []

    def show_all_books(self):
        os.system('clear')
        if len(self.books) == 0:
            print("There are no books added yet..")

        for i in range(len(self.books)):
            print(f"Id: {self.books[i].id} Title:{self.books[i].title}")

        input("Press [Enter] to continue")
        
    def add_book(self):
        book = Book()
        book.title = input("Enter the title of the book: ") 
        book.category = input("Enter the category of the book: ") 
        book.author = input("Enter the author of the book: ") 
        book.total_pages = input("Enter the total pages of the book: ") 
        self.books.append(book)
        self.show_all_books()

    def remove_book(self):
        ...