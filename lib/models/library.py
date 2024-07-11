from models.__init__ import CONNECTION, CURSOR

class Library:

    def __init__(self, name, location, id=None):
        self.name       = name
        self.location   = location
        self.id         = id
    
    @classmethod
    def drop_table(cls):
        '''set our table/instance '''

        sql = """
            DROP TABLE IF EXISTS libraries;
        """

        CURSOR.execute(sql)
        CONNECTION.commit()

    @classmethod
    def create_table(cls):
        '''create our sql table/instance'''

        sql = """
        CREATE TABLE IF NOT EXISTS libraries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT

            
        );
        """

        CURSOR.execute(sql)
        CONNECTION.commit()

    def save(self):
        '''create an object/instance with attribute/rows'''

        sql = """
            INSERT INTO libraries (name , location)
            VALUES (? , ?);
        """

        CURSOR.execute(sql, (self.name, self.location) )
        CONNECTION.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def delete(cls, name):
        '''grab name and delete our object/instance'''

        sql = """
            DELETE FROM libraries
            WHERE name = ? ;
        """

        CURSOR.execute(sql, (name, ) )
        CONNECTION.commit()
    
    @classmethod
    def fetch(cls):
        '''fetch all libraries in Library class in sql'''

        sql ="""
            SELECT * FROM libraries ;
        """

        CURSOR.execute(sql)
        return CURSOR.fetchall()

    @classmethod
    def get_lib_id_from_name(cls, name):
        '''return id form name'''

        sql = """
            SELECT id FROM libraries
            WHERE name = ?;
        """

        CURSOR.execute(sql, (name, ) )
        name_x = CURSOR.fetchone()
        return name_x[0] if name_x else None



    @classmethod
    def get_lib_by_name(cls, lib_name):
        '''looking for one specific library'''

        sql = """SELECT name FROM libraries WHERE name = ? """
        CURSOR.execute(sql, (lib_name,))
        result = CURSOR.fetchone()
        return result[0] if result else None


