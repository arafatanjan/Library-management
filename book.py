import add_books
import view_all_books
import update_book
import delete_book

all_books = []

print("Welcome to Library Management System")
while True:
   
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update All Books")
    print("4. Delete All Books")
    
    menu = input("Select any number: ")
    
    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_book =update_book.update_book(all_books)
    elif menu == "4":
        delete_book= delete_book.delete_book(all_books)
    else:
        print("Choose a valid number")