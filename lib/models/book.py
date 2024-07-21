from models.__init__ import CONNECTION, CURSOR

class Book:

    all = {}

    def __init__(self, author, book_name, year, foreign_id, id=None):
        self.author = author
        self.book_name = book_name
        self.year = year
        self.foreign_id = foreign_id
        self.id = id

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError('author must be a str value')
        self._author = value

    @property
    def book_name(self):
        return self._book_name

    @book_name.setter
    def book_name(self, value):
        if not isinstance(value, str):
            raise ValueError('book name must be a str value')
        self._book_name = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError('year must be an int value')
        self._year = value

    @property
    def foreign_id(self):
        return self._foreign_id

    @foreign_id.setter
    def foreign_id(self, value):
        if not isinstance(value, int):
            raise ValueError('foreign id must be an int value')
        self._foreign_id = value

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONNECTION.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT,
                book_name TEXT,
                year INTEGER,
                foreign_id INTEGER,
                FOREIGN KEY (foreign_id) REFERENCES libraries(id)
            );
        """
        CURSOR.execute(sql)
        CONNECTION.commit()

    def save(self):
        sql = """
            INSERT INTO books (author, book_name, year, foreign_id)
            VALUES (?, ?, ?, ?);
        """
        CURSOR.execute(sql, (self.author, self.book_name, self.year, self.foreign_id))
        CONNECTION.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, author, book_name, year, foreign_id):
        new_book = cls(author, book_name, year, foreign_id)
        new_book.save()
        return new_book

    def update(self):
        sql = """
            UPDATE books
            SET author = ?, book_name = ?, year = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.author, self.book_name, self.year, self.id))
        CONNECTION.commit()

    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONNECTION.commit()
        del type(self).all[self.id]

    @classmethod
    def instance_from_db(cls, row):
        obj_instance = cls.all.get(row[0])
        if obj_instance:
            obj_instance.id = row[0]
            obj_instance.author = row[1]
            obj_instance.book_name = row[2]
            obj_instance.year = row[3]
            obj_instance.foreign_id = row[4]
        else:
            obj_instance = cls(row[1], row[2], row[3], row[4])
            obj_instance.id = row[0]
            cls.all[obj_instance.id] = obj_instance
        return obj_instance

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM books
            WHERE id = ?;
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, book_name):
        sql = """
            SELECT * FROM books
            WHERE book_name = ?;
        """
        row = CURSOR.execute(sql, (book_name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_foreign_id(cls, fid):
        sql = """
            SELECT * FROM books
            WHERE foreign_id = ?;
        """
    
        rows = CURSOR.execute(sql, (fid, )).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    