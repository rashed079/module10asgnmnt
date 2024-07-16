from book_manager import add_book, remove_book, view_books, search_books_by_title_or_isbn, search_books_by_author
from loan_manager import lend_book, return_book, view_lent_books
from file_manager import load_data, save_data

def main():
    load_data()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. View All Books")
        print("4. Search Books")
        print("5. Search Books by Author")
        print("6. Lend a Book")
        print("7. Return a Book")
        print("8. View Lent Books")
        print("9. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            view_books()
        elif choice == '4':
            search_books_by_title_or_isbn()
        elif choice == '5':
            search_books_by_author()
        elif choice == '6':
            lend_book()
        elif choice == '7':
            return_book()
        elif choice == '8':
            view_lent_books()
        elif choice == '9':
            save_data()
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()