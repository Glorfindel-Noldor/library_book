from models.library import Library
from models.book import Book

def quit_menu():
    print('Thank you, goodbye!')

def view_all_libraries():
    libraries = Library.get_all()
    if not libraries:
        print('No libraries available.')
    for lib in libraries:
        print(f"ID: {lib[0]}, Name: {lib[1]}")

def add_library():
    name = input("Enter the name of the library: ")
    library = Library(name)
    library.save()
    print(f"Library '{name}' added with ID: {library.id}")

def delete_library():
    view_all_libraries()
    id_ = input('Enter the ID of the library to delete: ')
    try:
        id_ = int(id_)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    Library.delete_library(id_)
    print(f"Library with ID: {id_} successfully deleted.")

def view_all_books():
    books = Book.get_all()
    if not books:
        print('No books available.')
    for book in books:
        print(f"ID: {book[0]}, Name: {book[1]}, Library ID: {book[2]}")

def add_book():
    view_all_libraries()
    name = input('Enter the name of the book: ')
    library_id = input('Enter the library ID: ')
    try:
        library_id = int(library_id)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    book = Book(name, library_id)
    book.save()
    print(f"Book '{name}' added with ID: {book.id}")

def view_books_in_library():
    view_all_libraries()
    library_id = input('Enter the library ID to view its books: ')
    try:
        library_id = int(library_id)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    library = Library.find_by_id(library_id)
    if not library:
        print(f"No library found with ID: {library_id}")
        return
    books = library.get_books()
    if not books:
        print(f"No books found for library ID: {library_id}")
    for book in books:
        print(f"ID: {book[0]}, Name: {book[1]}")