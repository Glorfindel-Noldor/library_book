from models.__init__ import CONNECTION, CURSOR

class Book:

    def __init__(self, author, book_name, year, foreign_id , id = None):
        self.author     = author
        self.book_name  = book_name
        self.year       = year
        self.foreign_id = foreign_id
        self.id         = id

    @classmethod
    def drop_table(cls):
        '''set our table/instance'''

        sql = """
            DROP TABLE IF EXISTS books;
        """

        CURSOR.execute(sql)
        CONNECTION.commit()

    @classmethod
    def create_table(cls):
        ''' create our sql instance/object columns/attributes '''

        sql = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            author TEXT NOT NULL,
            book_name TEXT,
            year INTEGER,
            foreign_id INTEGER,
            FOREIGN KEY (foreign_id) REFERENCES libraries(id)
        );
        """
        CURSOR.execute(sql)
        CONNECTION.commit()

    def save(self):
        '''create an object/instance with attributes/rows'''

        sql = """
            INSERT INTO books (author, book_name , year, foreign_id)
            VALUES (? , ? , ? , ?);
        """

        CURSOR.execute(sql, (self.author, self.book_name, self.year , self.foreign_id) )
        CONNECTION.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def delete(cls, name_of_book):
        '''delete a book by author by id'''

        sql = """
            DELETE FROM books
            WHERE book_name = ?;
        """

        CURSOR.execute(sql, (name_of_book, ) )
        CONNECTION.commit()
    
    @classmethod
    def delete_all_in_lib(cls, lib_id):
        '''delete all books with the same library id'''

        sql = """
            DELETE FROM books
            WHERE foreign_id = ? ;
        """

        CURSOR.execute(sql, (lib_id, ) )
        CONNECTION.commit()

    @classmethod
    def fetch_by_foreign_id(cls, foreign_id ):
        '''grab a collection of books with the same foreign id'''

        sql = """
            SELECT * FROM books WHERE foreign_id = ? ;
        """

        CURSOR.execute(sql, (foreign_id, ) )
        return CURSOR.fetchall()

