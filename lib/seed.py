from models.library import Library
#from models.book import Book

# Create tables
Library.drop_table()
Library.create_library_table()
#Book.create_book_table()

print("Database tables created successfully.")