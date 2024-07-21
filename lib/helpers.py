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
        visit_library(lib_list[selection].name)
    except ValueError:
        print('the selection must be integer value or with in range')

def add_library():
    try:
        name = input('what is the name of the library?\n:')
        location = input('where is this library located (country only)?\n:')
        if not (name, location):
            raise ValueError
        Library.create(name, location)
    except ValueError:
        print('please enter name and location of library....')
    while True:
        go_to = input('go to this library now ?\n(y/n)\t').lower()
        match go_to:
            case ('y' | 'yes'):
                visit_library(name)
            case ('n' | 'no'):
                return
            case _:
                print('invalide choice, type `y` or `n` ')

def visit_library(selected_library):
    library = Library.find_by_name(selected_library)
    if not library:
        print("Library not found")
        return
    id = library.id
    name = library.name
    location = library.location

    books = library.books()
    if not books:
        print('No books')
    else:
        for i, book in enumerate(books, start=1):
            print(f"[{i}]\t{book.book_name}")

    while True:
        print(f"\t\t\tLibrary Name:\t{name}")
        print(f"\t\t\tLocation:\t{location}")

        print('0) Go back')
        print('u) Update info')
        print('a) Add a book')
        print('d) Delete this library')

        try:
            switch = input('Choose an option....\n:')
            match switch:
                case 'u':
                    update_library(id)
                case 'a':
                    add_book(id)
                case 'd':
                    delete_library(id)
                case '0':
                    from cli import menu
                    return menu()
                case _:
                    raise ValueError
        except ValueError:
            print('Selection must be string based or must be an option')

def update_library(lib_id):
    old_info = Library.find_by_id(lib_id)
    if not old_info:
        print("Library not found")
        return
    
    old_name    = old_info.name
    old_location= old_info.location

    try:
        new_name    = input('New name of library:\t')
        new_location= input('New location of library:\t')

        if not new_name:
            new_name        = old_name
        if not new_location:
            new_location    = old_location
        
        old_info.name       = new_name    #look into their attribute to change
        old_info.location   = new_location#look into their attribute to change
        old_info.update()


    except ValueError:
        print('Name and location must be strings')
    visit_library(new_name)

#----------------------------------------

def delete_library(lib_id):
    pass

def add_book(foreign_id):
    try:
        author = input('Author of book\n:')
        book_name = input('Name of book\n:')
        year = int(input('Year it came out\n:'))
    except ValueError:
        print('Incorrect value for year')
        return  # Exit the function if there's an error

    new_book = Book.create(author, book_name, year, foreign_id)
    if new_book:
        print('Book added successfully!')
    else:
        print('Failed to add book')

def view_book(book_id):
    pass

def update_book(book_id):
    pass

def delete_book(book_id):
    pass

def view_all_books(foreign_id):
    pass










