from models.__init__ import CONNECTION, CURSOR

class Book:

    def __init__(self, author, year ,foreign_id, id=None):
        self.author = author
        self.year   = year
        self.foreign_id = foreign_id
        self.id = id

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
            INSERT INTO books (author , year)
            VALUES (? , ?);
        """

        CURSOR.execute(sql, (self.author, self.year) )
        CONNECTION.commit()


    @classmethod
    def delete(cls, name):
        '''delete a book by author'''

        sql = """
            DELETE FROM books
            WHERE author = ?;
        """

        CURSOR.execute(sql, (name, ) )
        CONNECTION.commit()
    
    @classmethod
    def delete_all_in_lib(cls, lib_id):
        '''delete all books with the same library id'''

        sql = """
            DELETE FROM books
            WHERE foreign_id = ?
        """

        CURSOR.execute(sql, (lib_id, ) )
        CONNECTION.commit()

