from utils import Book

books = []

def add_book():
    title = input("Enter the book title: ")
    authors = input("Enter the authors (comma separated): ").split(',')
    isbn = input("Enter the ISBN: ")
    year = input("Enter the publishing year: ")
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    book = Book(title, [author.strip() for author in authors], isbn, year, price, quantity)
    books.append(book)
    print(f"Book '{title}' added successfully.")

def remove_book():
    title_or_isbn = input("Enter the book title or ISBN to remove: ")
    for book in books:
        if book.title == title_or_isbn or book.isbn == title_or_isbn:
            books.remove(book)
            print(f"Book '{title_or_isbn}' removed successfully.")
            return
    print("Book not found.")

def view_books():
    if not books:
        print("No books available.")
        return
    for book in books:
        print(f"Title: {book.title}, Authors: {', '.join(book.authors)}, ISBN: {book.isbn}, Year: {book.year}, Price: ${book.price:.2f}, Quantity: {book.quantity}")

def search_books_by_title_or_isbn():
    term = input("Enter the title or ISBN to search: ")
    found_books = [book for book in books if term in book.title or term in book.isbn]
    if not found_books:
        print("No books found.")
    else:
        for book in found_books:
            print(f"Title: {book.title}, Authors: {', '.join(book.authors)}, ISBN: {book.isbn}, Year: {book.year}, Price: ${book.price:.2f}, Quantity: {book.quantity}")

def search_books_by_author():
    author_name = input("Enter the author's name to search: ")
    found_books = [book for book in books if author_name in ', '.join(book.authors)]
    if not found_books:
        print("No books found.")
    else:
        for book in found_books:
            print(f"Title: {book.title}, Authors: {', '.join(book.authors)}, ISBN: {book.isbn}, Year: {book.year}, Price: ${book.price:.2f}, Quantity: {book.quantity}")