import sqlite3

class MaintenanceRecord:
    def __init__(self, id, equipment_id, maintenance_date, description, performed_by):
        self.id = id
        self.equipment_id = equipment_id
        self.maintenance_date = maintenance_date
        self.description = description
        self.performed_by = performed_by

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS maintenance_record (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        equipment_id INTEGER,
                        maintenance_date TEXT,
                        description TEXT,
                        performed_by TEXT,
                        FOREIGN KEY (equipment_id) REFERENCES equipment(id))''')
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, equipment_id, maintenance_date, description, performed_by):
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''INSERT INTO maintenance_record (equipment_id, maintenance_date, description, performed_by)
                     VALUES (?, ?, ?, ?)''', (equipment_id, maintenance_date, description, performed_by))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM maintenance_record''')
        rows = c.fetchall()
        conn.close()
        return [cls(*row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM maintenance_record WHERE id=?''', (id,))
        row = c.fetchone()
        conn.close()
        return cls(*row) if row else None

    @classmethod
    def delete(cls, id):
        conn = sqlite3.connect('cli.db')
        c = conn.cursor()
        c.execute('''DELETE FROM maintenance_record WHERE id=?''', (id,))
        conn.commit()
        conn.close()
