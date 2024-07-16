from utils import Loan

loans = []

def lend_book():
    isbn = input("Enter the ISBN of the book to lend: ")
    for book in books:
        if book.isbn == isbn and book.quantity > 0:
            borrower = input("Enter the name of the borrower: ")
            book.quantity -= 1
            loans.append(Loan(book, borrower))
            print(f"Book '{book.title}' lent to {borrower}.")
            return
    print("Book not available for lending or not found.")

def return_book():
    isbn = input("Enter the ISBN of the book to return: ")
    for loan in loans:
        if loan.book.isbn == isbn:
            loan.book.quantity += 1
            loans.remove(loan)
            print(f"Book '{loan.book.title}' returned successfully.")
            return
    print("No such book loaned.")

def view_lent_books():
    if not loans:
        print("No books have been lent.")
    else:
        for loan in loans:
            print(f"Book Title: {loan.book.title}, Borrower: {loan.borrower}")