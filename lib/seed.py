def run_seeding():
    from models.library import Library
    from models.book import Book


    #Create tables
    Library.drop_table()
    Book.drop_table()
    
    Library.create_table()
    Book.create_table()

    lib1 = Library.create('Alexandria', 'Egypt')
    lib2 = Library.create('Damascus', 'Syria')

    book1 = Book.create('tim', 'tim is awesome', 1889, lib2.id)
    book2 = Book.create('fiona', 'fiona is number one', 1998, lib2.id)

    book3 = Book.create('shrek', 'how to be like me', 2007, lib1.id)






    print("Database tables created successfully and data seeded.")






if __name__ == "__main__":
    run_seeding()
