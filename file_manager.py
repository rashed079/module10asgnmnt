from utils import Book, Loan
import json

def load_data():
    global books, loans
    try:
        with open('library_data.json', 'r') as file:
            data = json.load(file)
            books = [Book(**book) for book in data['books']]
            loans = [Loan(Book(**loan['book']), loan['borrower']) for loan in data['loans']]
    except FileNotFoundError:
        books = []
        loans = []

def save_data():
    data = {
        'books': [book.__dict__ for book in books],
        'loans': [{'book': loan.book.__dict__, 'borrower': loan.borrower} for loan in loans]
    }
    with open('library_data.json', 'w') as file:
        json.dump(data, file, indent=4)