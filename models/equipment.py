import sqlite3

class Equipment:
    def __init__(self, id, name, type, serial_number):
        self.id = id
        self.name = name
        self.type = type
        self.serial_number = serial_number

    @classmethod
    def create_table(cls):
        """
        Create the 'equipment' table in the database if it doesn't exist.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS equipment (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        type TEXT,
                        serial_number TEXT)''')
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, name, type, serial_number):
        """
        Insert a new equipment record into the 'equipment' table.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''INSERT INTO equipment (name, type, serial_number)
                     VALUES (?, ?, ?)''', (name, type, serial_number))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """
        Retrieve all equipment records from the 'equipment' table.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM equipment''')
        rows = c.fetchall()
        conn.close()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """
        Find an equipment record by its ID in the 'equipment' table.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM equipment WHERE id=?''', (id,))
        row = c.fetchone()
        conn.close()
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id):
        """
        Delete an equipment record by its ID from the 'equipment' table.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''DELETE FROM equipment WHERE id=?''', (id,))
        conn.commit()
        conn.close()
