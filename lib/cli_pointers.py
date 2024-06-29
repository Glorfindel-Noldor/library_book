from models.library import Library

def quit_menu():
    print('Thank you, goodbye!')

def name_library():
    name_arg = input("Enter the name of the library: ")
    library = Library(name_arg)
    library.save()
    print(f"Library '{name_arg}' added with ID: {library.id}")

def delete_library_name():
    arg_id = input('ID of library you would like to delete:\t')
    try:
        arg_id = int(arg_id)
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return
    Library.delete_library(arg_id)
    print(f"Library with ID: {arg_id} successfully deleted.")