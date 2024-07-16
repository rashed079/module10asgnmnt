class Book:
    def __init__(self, title, authors, isbn, year, price, quantity):
        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.year = year
        self.price = price
        self.quantity = quantity

class Loan:
    def __init__(self, book, borrower):
        self.book = book
        self.borrower = borrower
