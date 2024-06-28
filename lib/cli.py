#!/usr/bin/env python3.12
import cli_pointers


def menu():
    while True:
        print('0.\tQuit')
        print('1.\tView all libraries')
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
                print('All branches displayed !!!!')
            case _:
                print('Invalid choice')

if __name__ == "__main__":
    menu()