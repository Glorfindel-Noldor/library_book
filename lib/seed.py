from models.library import Library
from models.book import Book
import cli_pointers
import ipdb


def run_seeding():
    # Create tables
    Library.drop_table()
    Book.drop_table()

    Library.create_library_table()
    Book.create_table()



    print("Database tables created successfully and data seeded.")

    ipdb.set_trace()






if __name__ == "__main__":
    run_seeding()



