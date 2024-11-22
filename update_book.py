from save_all_books import save_all_books

def update_book(all_books):
    if len(all_books) == 0:
        print("No books available to update.")
        return all_books

    isbn_to_update = int(input("Enter the ISBN of the book you want to update: "))
    book_found = False

    for book in all_books:
        if book['isbn'] == isbn_to_update:
            book_found = True
            print("Book found. Enter new details or press Enter to skip updating a field.")
            title = input(f"Enter new title (current: {book['title']}): ") or book['title']
            author = input(f"Enter new author (current: {book['author']}): ") or book['author']
            year = input(f"Enter new year (current: {book['year']}): ") or book['year']
            price = input(f"Enter new price (current: {book['price']}): ") or book['price']
            quantity = input(f"Enter new quantity (current: {book['quantity']}): ") or book['quantity']

            book.update({
                "title": title,
                "author": author,
                "year": int(year),
                "price": int(price),
                "quantity": int(quantity),
            })
            print("Book updated successfully.")
            break

    if not book_found:
        print(f"No book found with ISBN {isbn_to_update}.")
    
    save_all_books(all_books)
    return all_books