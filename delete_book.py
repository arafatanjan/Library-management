from save_all_books import save_all_books

def delete_book(all_books):
    if len(all_books) == 0:
        print("No books available to delete.")
        return all_books

    isbn_to_delete = int(input("Enter the ISBN of the book you want to delete: "))
    book_found = False

    for book in all_books:
        if book['isbn'] == isbn_to_delete:
            book_found = True
            all_books.remove(book)
            print(f"Book with ISBN {isbn_to_delete} has been deleted.")
            break

    if not book_found:
        print(f"No book found with ISBN {isbn_to_delete}.")
    
    save_all_books(all_books)
    return all_books