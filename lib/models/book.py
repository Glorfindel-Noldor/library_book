from models.__init__ import CONNECTION, CURSOR


error_message = 'There has yet to be a library to be created it seems. please create one before creating a book'


class Book:
    def __init__ (self, name,foreign_id = None, id_ = None ):
        self.name = name
        self.id_ = id_
        self.foreign_id = foreign_id or self.get_default_id()


    @classmethod
    def drop_table(cls):
        '''Drop the Book table for clearing purposes'''
        sql = "DROP TABLE IF EXISTS books;"
        CURSOR.execute(sql)
        CONNECTION.commit()


    @classmethod
    def create_table(cls):
        '''Create the Books table'''
        sql = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            foreign_id INTEGER,
            FOREIGN KEY (foreign_id) REFERENCES libraries(id)
        );
        """
        CURSOR.execute(sql)
        CONNECTION.commit()


    def save(self):
        """create a book and save to the table of library """
        sql = """
            INSERT INTO books (name, foreign_id ) VALUES ( ? , ? );
        """

        CURSOR.execute(sql, (self.name, self.foreign_id))
        CONNECTION.commit()
        self.id = CURSOR.lastrowid
        

    @staticmethod
    def get_default_id():
        '''grabs a default id from an existing library table '''

        sql = """SELECT id FROM libraries LIMIT 1;"""
        CURSOR.execute(sql)
        id_ = CURSOR.fetchone()
        if id_ :
            return id_[0]
        else :
            print(error_message)
            
        
        




