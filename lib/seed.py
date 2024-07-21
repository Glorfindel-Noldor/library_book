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
    








    print("Database tables created successfully and data seeded.")






if __name__ == "__main__":
    run_seeding()
