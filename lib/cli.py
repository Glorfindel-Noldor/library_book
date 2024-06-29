#!/usr/bin/env python3.12

import cli_pointers
from models.library import Library

def menu():
    while True:
        print('0.\tQuit')
        print('1.\tView all libraries')
        print('2.\tAdd a new library')
        print('3\tDelete existing library')
        switch = input('Select from the following menu: ')

        try:
            switch = int(switch)
        except ValueError:
            print('Invalid input, please enter a number.')
            continue  # Ask for input again

        match switch:
            case 0:
                cli_pointers.quit_menu()
                break  # Exit the loop
            case 1:
                libraries = Library.get_all()
                for lib in libraries:
                    print(f"ID: {lib[0]}, Name: {lib[1]}")
            case 2:
                cli_pointers.name_library()
            case 3:
                cli_pointers.delete_library_name()
            case _:
                print('Invalid choice')

if __name__ == "__main__":
    menu()