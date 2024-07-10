#!/usr/bin/env python3.12
import lib.helpers as helpers
from models.library import Library
from models.book import Book

def menu():
    while True:
        print('0.\tQuit')

        switch = input('Select from the following menu: ')

        try:
            switch = int(switch)
        except ValueError:
            print('Invalid input, please enter a number.')
            continue  # Ask for input again

        match switch:
            case 0:
                helpers.quit_menu()
                break  # Exit the loop
            case _:
                print('Invalid choice')

if __name__ == "__main__":
    menu()
