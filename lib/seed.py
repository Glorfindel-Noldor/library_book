from models.library import Library
from models.book import Book

def run_seeding():
    # Create tables
    Library.drop_table()
    Book.drop_table()
    Library.create_library_table()
    Book.create_table()
    print("Database tables created successfully.")




run_seeding()

