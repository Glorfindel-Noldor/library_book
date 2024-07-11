from os import system as clear_menu
from models.library import Library
from models.book import Book

def view_libraries():
    clear_menu('clear')
    libraries = Library.fetch()
    if libraries:
        print('name:\t\t\tlocation:')
        for lib in libraries:
            print(f"{lib[1]}\t:\t{lib[2]}")
    else:
        print('there are no libraries, try creating one with option `2`')
        return
    
    try:
        name_of_library = input('\nEnter name of library you`d like to visit.\n:').lower()
        library = Library.get_lib_by_name(name_of_library)
        if library:
            enter_library(name_of_library)
            print('name:\t\t\tlocation:')
            for lib in libraries:
                print(f"{lib[1]}\t:\t{lib[2]}")
        else:
            raise ValueError
    except ValueError:
        print('library not found. ')

def enter_library(lib_name):


     from cli import menu
     #the user brings name_of_library here from view_libraries as lib_name
     lib_id = Library.get_lib_id_from_name(lib_name)
    # now that that lib_name is now lib_id we can bring all books of same foreign id
     fetch_books =  Book.fetch_by_foreign_id(lib_id)
    #fetch books is a list of books

     while True:
#        if fetch_books != []:
#            for book in fetch_books:
#                print(f"Author: {book[1]} Title: {book[2]}")
#        else: None
        print('1. add a book')
        print('2. delete a book')
        print('3. view all books')
        print('4. go back ')
        try:
            switch = int(input('make a choice...\t'))
        except ValueError:
            print('must be int not str choice')
            continue

        match switch:
            case 1:
                add_a_book(lib_id)
                #we will need the 'lib_id' as a foreign_id
            case 2:
                 delete_book(lib_id) if fetch_books else print('no books to delete try adding one')
            case 3:
                view_all_books(lib_id)
            case 4:
                menu()
            case _:
                print('not an option.')

def add_library():
    new_name     = input('name of library.\n:').lower()
    new_location = input('where is this library located?\n:').lower()

    if isinstance((new_name), str) and  isinstance( new_location, str):
        new_library = Library(new_name, new_location)
        new_library.save()
        print(f"new library {new_name} created in {new_location}!")
    else:
        print('please enter str nothing was created.')
        return

def add_a_book(lib_id_as_foreign_id):
    
    author = input('name of author\t:').lower()
    book_name = input('name of book\t:').lower()
    year= input('year book came out\t:')
    
    new_book= Book(author, book_name, year, lib_id_as_foreign_id)
    new_book.save()

def view_all_books(lib_id):
    books = Book.fetch_by_foreign_id(lib_id)
    if not books:
        print('no books yet, try adding some ?')
    else:
        print('author\t:\tname of book')
        for book in books:
            print(f"{book[1]}\t:\t{book[2]}")

def delete_book(lib_id):

    show_me_all_books = Book.fetch_by_foreign_id(lib_id)
    if not show_me_all_books:
        print('\nno books to delete...\n')
    for lib in show_me_all_books:
        print(f"author: {lib[1]}\tname of book: {lib[2]}")
    if show_me_all_books:
        deleted_by_name = input('name of book you`d like to delete please.\n:').lower()
    else:
        return ValueError
    try:
        Book.delete(deleted_by_name)
    except ValueError:
        print('That book does not exist here check other libraries perhaps.')

def delete_library():
    list_of_libraries = Library.fetch()
    if not list_of_libraries:
        print('no libraries to delete. try adding one first with option `1`')
        return
    print('name:\t\t\tlocation:')
    for lib in list_of_libraries:
        print(f"{lib[1]}\t:\t{lib[2]} ")
    
    try:

        to_delete = input('which library would you like to delete?\n:').lower()
        lib_id = Library.get_lib_id_from_name(to_delete)
        double_check = input('warning if you delete this library you will also delete the books in it, are you sure?\n( y / n ):\t').lower()
        if double_check.lower() == ('y' or 'yes'):
            Book.delete_all_in_lib(lib_id)
            Library.delete(to_delete)
            print('DELETED LIBRARY AND ANY BOOKS IN IT!')
        elif double_check.lower() == ('n' or 'no'):
            print('nothing deleted!')
        else:
            print('error in choice nothing deleted')
    except ValueError:
        print('Library not found')
        
