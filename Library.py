import os
from book import Book

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
        os.system('clear')
        b = Book()
        b.title = input("Enter the title of the book: ") 
        b.category = input("Enter the category of the book: ") 
        b.author = input("Enter the author of the book: ") 
        b.total_pages = input("Enter the total pages of the book: ")

        not_answered = True
        while not_answered:
            os.system('clear')
            print("Are the following details correct? y/n")
            print(f"Title: {b.title}, Category {b.category}, Author: {b.author}, Total Pages: {b.total_pages}")
            
            choice = input().lower()
            if choice != "y" and choice != "n":
                continue

            not_answered = False

            if choice == "y":
                self.books.append(b)
                
            input("Press [Enter] to continue")


    def remove_book(self):
        deleteId = int(input("Give the Id of the book you want to remove: "))
        if not any(b for b in self.books if b.Id == deleteId):
            input("No book has been found with that Id")
            return
        self.books = [b for b in self.books if b.id != deleteId]
        input("Book has been deleted..")