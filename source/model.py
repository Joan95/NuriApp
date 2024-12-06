import sqlite3

class NutritionistModel:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pacients (
            pacient_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nom TEXT NOT NULL,
            cognoms TEXT NOT NULL,
            email TEXT NOT NULL,
            data_neixement DATE NOT NULL,
            sexe TEXT CHECK(sexe IN ('HOME', 'DONA'))
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Dietes (
            diet_id INTEGER PRIMARY KEY AUTOINCREMENT,
            pacient_id INTEGER NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE,
            description TEXT,
            FOREIGN KEY (pacient_id) REFERENCES Pacients(pacient_id)
        )
        ''')
        self.conn.commit()

    def add_user(self, name, lastname, email, birthdate, gender):
        self.cursor.execute('''
        INSERT INTO Pacients (nom, cognoms, email, data_neixement, sexe)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, lastname, email, birthdate, gender))
        self.conn.commit()

    def get_users(self):
        self.cursor.execute('SELECT nom, cognoms FROM Pacients')
        return [{'name': row[0], 'lastname': row[1]} for row in self.cursor.fetchall()]

    def add_diet(self, pacient_id, start_date, end_date, description):
        self.cursor.execute('''
        INSERT INTO Dietes (pacient_id, start_date, end_date, description)
        VALUES (?, ?, ?, ?)
        ''', (pacient_id, start_date, end_date, description))
        self.conn.commit()

    def get_patient_id(self, name, lastname):
        self.cursor.execute('SELECT pacient_id FROM Pacients WHERE nom=? AND cognoms=?', (name, lastname))
        return self.cursor.fetchone()[0]

    def get_current_diet(self, pacient_id):
        self.cursor.execute('''
        SELECT start_date, end_date, description FROM Dietes
        WHERE pacient_id=? ORDER BY start_date DESC LIMIT 1
        ''', (pacient_id,))
        row = self.cursor.fetchone()
        if row:
            return {'start_date': row[0], 'end_date': row[1], 'description': row[2]}
        return None

    def close(self):
        self.conn.close()
