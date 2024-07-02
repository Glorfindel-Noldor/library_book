#!/usr/bin/env python3.12

import cli_pointers
from models.library import Library
from models.book import Book

def menu():
    while True:
        print('0.\tQuit')
        print('1.\tView all libraries')
        print('2.\tAdd a new library')
        print('3.\tDelete an existing library')
        print('4.\tView all books')
        print('5.\tAdd a new book')
        print('6.\tView books in a library')
        switch = input('Select from the following menu: ')

        try:
            switch = int(switch)
        except ValueError:
            print('Invalid input, please enter a number.')
            continue

        match switch:
            case 0:
                cli_pointers.quit_menu()
                break
            case 1:
                cli_pointers.view_all_libraries()
            case 2:
                cli_pointers.add_library()
            case 3:
                cli_pointers.delete_library()
            case 4:
                cli_pointers.view_all_books()
            case 5:
                cli_pointers.add_book()
            case 6:
                cli_pointers.view_books_in_library()
            case _:
                print('Invalid choice')

if __name__ == "__main__":
    menu()