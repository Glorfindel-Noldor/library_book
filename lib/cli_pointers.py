from models.__init__ import CONNECTION , CURSOR
from models.library import Library
from models.book import Book

default_lib_msg = 'the library id you provided was not found. placed in default library'

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
    id_ = input('id of library ?')
    try :
        if id_ in Library.all.index:
            book = Book(new_book, id_ or foreign_id)
            book.save()
            print(f"{new_book}: has been created.")
        else:
            book = Book(new_book, id_ or foreign_id)
            book.save()
            print(f"{new_book}: ,{default_lib_mesg}")
    except Exception as e: 
        print(e)




