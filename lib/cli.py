#!/usr/bin/env python3.12
from helpers import (view_libraries , add_library, delete_library)


def menu():
    while True:
        print('0.\tQuit')
        print('1.\tView libraries.')
        print('2.\tAdd a library.')
        print('3.\tDelete a library.')
        switch = input('Select from the following menu: ')

        try:
            switch = int(switch)
        except ValueError:
            print('Invalid input, please enter a number.')
            continue  # Ask for input again

        match switch:
            case 0:
                print('thank you goodbye')
                return None
            case 1:
                view_libraries()
            case 2:
                add_library()
            case 3:
                delete_library()
            case _:
                print('Invalid choice')

def main():
    menu()
if __name__ == "__main__":
    main()



