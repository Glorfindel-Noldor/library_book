from os import system as clear_menu
from models.library import Library
from models.book import Book

def choosing_library():
    lib_list = Library.get_all()
    if not lib_list:
        print('no libraries, try creating one first!')
        return
    for i , lib in enumerate(lib_list, start=1):
        print(f"[{i}]\t{lib.name}")
    
    try:
        selection = int(input('select the number next to the library in which you`d like to visit.'))-1
        if 1 > selection > len(lib_list):
            raise ValueError
        visit_library(lib_list[selection].id)
    except ValueError:
        print('the selection must be integer value or with in range')

def add_library():
    try:
        name = input('What is the name of the library?\n:')
        location = input('Where is this library located (country only)?\n:')
        
        if not name:
            raise ValueError
        if not location:
            raise ValueError
        
        Library.create(name, location)
    except ValueError:
        print('can not leave name or location blank, nothing created !')
        return

    while True:
        go_to = input('Go to this library now?\n(y/n)\t').lower()
        match go_to:
            case ('y' | 'yes'):
                lib = Library.find_by_name(name)
                visit_library(lib.id)
            case ('n' | 'no'):
                return
            case _:
                print('Invalid choice, type `y` or `n` ')

def visit_library(selected_library):
    clear_menu('clear')
    library = Library.find_by_id(selected_library)
    if not library:
        print("Library not found")
        return

    while True:
        books = library.books()
        print(f"\t\t\tLibrary Name:\t{library.name}")
        print(f"\t\t\tLocation:\t{library.location}")

        print('b) Go back')
        print('u) Update library info')
        print('a) Add a book')
        print('d) Delete this library')
        print('Select a book to view by the number associated next to it.')
        if not books:
            print('No books')
        else:
            for i, book in enumerate(books, start=1):
                print(f"[{i}]\t{book.book_name}")
        
        switch = input('Choose an option....\n:')

        if switch.isdigit():
            switch = int(switch)
            if 1 <= switch <= len(books):
                view_book(books[switch - 1].id)
                continue 
        
        match switch:
            case 'u':
                update_library(library.id)
            case 'a':
                add_book(library.id)
            case 'd':
                delete_library(library)
                return  
            case 'b':
                from cli import menu
                return menu()
            case _:
                print('Invalid choice, must be a valid option')

def update_library(lib_id):
    library = Library.find_by_id(lib_id)
    if not library:
        print("Library not found")
        return
    
    try:
        new_name = input('New name of library:\t')
        new_location = input('New location of library:\t')

        if new_name:
            library.name = new_name
        if new_location:
            library.location = new_location
        
        library.update()
        print('Library updated successfully!')
    except ValueError:
        print('Name and location must be strings')
    visit_library(library.id)

def delete_library(library):
    try:
        switch = input('Are you sure you want to delete this? Doing so will also delete books in the library. (y/n):\t').lower()
        if switch in ('y', 'yes'):
            for book in library.books():
                book.delete()
            library.delete()
            print('DELETED!')
        elif switch in ('n', 'no'):
            print('Nothing was deleted')
        else:
            raise ValueError
    except ValueError:
        print('Option not acceptable, nothing deleted.')

def add_book(foreign_id):
    try:
        author = input('Author of book\n:')
        book_name = input('Name of book\n:')
        year = int(input('Year it came out\n:'))

        new_book = Book.create(author, book_name, year, foreign_id)
        if new_book:
            print('Book added successfully!')
        else:
            raise ValueError
    except ValueError:
        print('Incorrect value for year or values left blank')

def view_book(book_id):
    clear_menu('clear')
    book = Book.find_by_id(book_id)
    if not book:
        print('Book not found')
        return
    while True:
        print(f"Name of book: {book.book_name}\nAuthor: {book.author}\nYear released: {book.year}")
        print('u) Update')
        print('d) Delete')
        print('b) Go back')
        try:
            switch = input('Choose an option\n:')

            match switch:
                case 'u':
                    update_book(book.id)
                case 'd':
                    delete_book(book)
                    return
                case 'b':
                    visit_library(book.foreign_id)
                case _:
                    print('Must be a letter option')
        except ValueError:
            print('Not an option')

def update_book(book_id):
    book = Book.find_by_id(book_id)
    if not book:
        print("Book not found")
        return
    
    try:
        new_author = input('Update author\'s name:\t')
        new_book_name = input('Update book name:\t')
        new_year = input('Update year book came out:\t')

        if new_author:
            book.author = new_author
        if new_book_name:
            book.book_name = new_book_name
        if new_year:
            book.year = int(new_year)

        book.update()
        print('Book updated successfully!')
    except ValueError:
        print('Year must be an int value')

def delete_book(book):
    try:
        switch = input('Delete? (y/n)').lower()
        if switch in ('y', 'yes'):
            book.delete()
            visit_library(book.foreign_id)
        elif switch in ('n', 'no'):
            return
        else: 
            raise ValueError
    except ValueError:
        print('Error in deleting book option not accepted')