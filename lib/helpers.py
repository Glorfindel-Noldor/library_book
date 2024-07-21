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
    id = library.id
    name = library.name
    location = library.location

    while True:
        books = library.books()  # Fetch books within the loop to refresh the list after any changes
        print(f"\t\t\tLibrary Name:\t{name}")
        print(f"\t\t\tLocation:\t{location}")

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
                continue  # Continue after viewing a book to avoid the match case below
        
        match switch:
            case 'u':
                update_library(id)
            case 'a':
                add_book(id)
            case 'd':
                delete_library(id)
                return  # Exit after deleting the library
            case 'b':
                from cli import menu
                return menu()
            case _:
                print('Invalid choice, must be a valid option')

def update_library(lib_id):
    old_info = Library.find_by_id(lib_id)
    if not old_info:
        print("Library not found")
        return
    
    old_name    = old_info.name
    old_location= old_info.location

    try:
        old_author    = input('New name of library:\t')
        new_location= input('New location of library:\t')

        if not old_author:
            old_author        = old_name
        if not new_location:
            new_location    = old_location
        
        old_info.name       = old_author    #look into their attribute to change
        old_info.location   = new_location#look into their attribute to change
        old_info.update()


    except ValueError:
        print('Name and location must be strings')
    visit_library(old_author)

def delete_library(lib_id):

    try:
        switch = input('are you sure you want to delete this?\n Doing so will also delete books in library.\n(y/n):\t').lower()
        if switch in ('y' or 'yes'):
            lib = Library.find_by_id(lib_id)
            books = Book.find_by_foreign_id(lib_id)
            for book in books:
                book.delete()
            lib.delete()
            print('DELETED!')
        elif switch in ('n' or 'no'):
            print('nothing was deleted')
            return
        else: raise ValueError
    except ValueError:
        print('option not acceptable, nothing deleted.')

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
        return  # Exit the function if there's an error

def view_book(book_id):
    clear_menu('clear')
    book = Book.find_by_id(book_id)
    if not book:
        print('book not found')
        return
    library_id = book.foreign_id
    book_id = book.id
    name = book.book_name
    author = book.author
    year = book.year
    while True:
        print(f"name of book: {name}\nauthor: {author}\nyear released: {year}")
        print('u) update')
        print('d) delete')
        print('b) go back')
        try:
            switch = input('choose an option\n:')

            match switch:
                case 'u':
                    update_book(book_id)
                case 'd':
                    delete_book(book)
                    return
                case 'b':
                    visit_library(library_id)
                case _:
                    print('must be letter option')
        except ValueError:
            print('not an option')

def update_book(book_id):
    old_info = Book.find_by_id(book_id)
    if not old_info:
        print("Book not found")
        return
    
    old_author      = old_info.author
    old_book_name   = old_info.book_name
    old_year        = old_info.year
    # foreign_id:  this never has to be questioned and is implicitly brought in
    try:
        update_author    = input('update author`s name:\t')
        update_book_name= input('update book name:\t')
        update_year     = input('update year book came out:\t')
        if not update_author:
            update_author = old_author
        if not update_book_name:
            update_book_name = old_book_name
        if not update_year:
            update_year = old_year
        else:
            update_year = int(update_year)
        
        old_info.author = update_author
        old_info.book_name = update_book_name
        old_info.year = update_year
        old_info.update()

        print('book updated successfully!')
    except ValueError:
        print('year must be int value ')

def delete_book(book):
    try:
        switch = input('delete ? (y/n)').lower()
        if switch in ('y', 'yes'):
            book.delete()
            visit_library(book.foreign_id)
        elif switch in ('n', 'no'):
            return
        else: 
            raise ValueError
    except ValueError:
        print('error in deleting book option not accepted')
