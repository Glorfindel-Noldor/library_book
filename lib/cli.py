#!/usr/bin/env python3.12
import os
from seed import run_seeding
from helpers import (
    add_library,
    choosing_library
)


def menu():
    os.system('clear')
    while True:
        print('0.\tQuit')
        print('1.\tAdd Library')
        print('2.\tVisit Library.')

        switch = input('Select from the following menu: ')

        try:
            switch = int(switch)
        except ValueError:
            print('Invalid input, please enter a number.')
            continue  # Ask for input again

        match switch:
            case 1:
                add_library()
            case 2:
                choosing_library()
            case 0:
                print('thank you, goodbye')
                return
            case _:
                print('Invalid choice')

def main():
    run_seeding()
    menu()
if __name__ == "__main__":
    main()
