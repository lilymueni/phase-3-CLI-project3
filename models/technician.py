import sqlite3

class Technician:
    def __init__(self, id, name, specialization, contact_info):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.contact_info = contact_info

    @classmethod
    def create_table(cls):
        """
        Create the 'technician' table in the database if it doesn't exist.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS technician (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        specialization TEXT,
                        contact_info TEXT)''')
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, name, specialization, contact_info):
        """
        Insert a new technician record into the 'technician' table.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''INSERT INTO technician (name, specialization, contact_info)
                     VALUES (?, ?, ?)''', (name, specialization, contact_info))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """
        Retrieve all technician records from the 'technician' table.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM technician''')
        rows = c.fetchall()
        conn.close()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """
        Find a technician record by its ID in the 'technician' table.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM technician WHERE id=?''', (id,))
        row = c.fetchone()
        conn.close()
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id):
        """
        Delete a technician record by its ID from the 'technician' table.
        """
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''DELETE FROM technician WHERE id=?''', (id,))
        conn.commit()
        conn.close()
