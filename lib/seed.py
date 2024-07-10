from models.library import Library
from models.book import Book
import ipdb # type: ignore


def run_seeding():
    # Create tables
    Library.drop_table()
    Book.drop_table()

    Library.create_table()
    Book.create_table()

    print("Database tables created successfully and data seeded.")

    ipdb.set_trace()






if __name__ == "__main__":
    run_seeding()
