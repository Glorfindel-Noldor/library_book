from models.__init__ import CONNECTION, CURSOR

class Library:

    all = {}

    def __init__(self, name, location, id=None):
        self.name = name
        self.location = location
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be a str value')
        self._name = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise ValueError('location must be a str value')
        self._location = value

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS libraries;
        """
        CURSOR.execute(sql)
        CONNECTION.commit()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS libraries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                location TEXT
            );
        """
        CURSOR.execute(sql)
        CONNECTION.commit()

    def save(self):
        sql = """
            INSERT INTO libraries (name, location)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONNECTION.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location):
        new_library = cls(name, location)
        new_library.save()
        return new_library

    def update(self):
        sql = """
            UPDATE libraries
            SET name = ?, location = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONNECTION.commit()

    def delete(self):
        sql = """
            DELETE FROM libraries
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
            obj_instance.name = row[1]
            obj_instance.location = row[2]
        else:
            obj_instance = cls(row[1], row[2])
            obj_instance.id = row[0]
            cls.all[obj_instance.id] = obj_instance
        return obj_instance

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM libraries
            WHERE id = ?;
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM libraries
            WHERE name = ?;
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def books(self):
        from models.book import Book
        sql = """
            SELECT * FROM books
            WHERE foreign_id = ?;
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Book.instance_from_db(row) for row in rows]

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM libraries;
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

