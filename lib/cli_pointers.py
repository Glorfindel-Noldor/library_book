from models.__init__ import CONNECTION, CURSOR
from models.library import Library
from models.book import Book

default_lib_msg = 'The library ID you provided was not found. Placed in default library.'

def quit_menu():
    print('Thank you, goodbye!')

def name_library():
    name_arg = input("Enter the name of the library: ")
    library = Library(name_arg)
    library.save()
    print(f"Library '{name_arg}' added with ID: {library.id}")

def delete_library_name():
    CURSOR.execute("SELECT * FROM libraries")
    libs = CURSOR.fetchall()

    if not libs:
        print('No libraries to delete.')
        return

    arg_id = input('ID of library you would like to delete:\t')

    try:
        arg_id = int(arg_id)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    Library.delete_library(arg_id)
    print(f"Library with ID: {arg_id} successfully deleted.")

def add_book():
    foreign_id = Book.get_default_id()
    if foreign_id is None:
        print('No book created: There is no existing library. Please create a library first.')
        return

    new_book = input('What is the name of the book?: ')
    id_ = input('ID of library? ')

    try:
        id_ = int(id_)
        if Library.find_by_id(id_):
            book = Book(name=new_book, foreign_id=id_ or foreign_id)
            book.save()
            print(f"{new_book}: has been created.")
        else:
            book = Book(name=new_book, foreign_id=foreign_id)
            book.save()
            print(f"{new_book}: ,{default_lib_msg}")
    except Exception as e:
        print(e)

def view_books_in_library():
    libraries = Library.get_all()
    if not libraries:
        print('No libraries available.')
        return

    for lib in libraries:
        print(f"ID: {lib[0]}, Name: {lib[1]}")
    
    library_id = input("Enter the library ID to view its books: ")

    try:
        library_id = int(library_id)
        library = Library.find_by_id(library_id)
        if library:
            books = library.get_books()
            if books:
                for book in books:
                    print(f"ID: {book[0]}, Name: {book[1]}")
            else:
                print('No books found in this library.')
        else:
            print('Library not found.')
    except ValueError:
        print("Invalid ID. Please enter a number.")
