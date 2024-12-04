import sqlite3

class NutritionistModel:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Usuaris (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT,
            birthdate DATE,
            gender TEXT CHECK(gender IN ('MALE', 'FEMALE'))
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Dietes (
            diet_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            start_date DATE NOT NULL,
            end_date DATE,
            description TEXT,
            FOREIGN KEY (user_id) REFERENCES Usuaris(user_id)
        )
        ''')
        self.conn.commit()

    def add_user(self, name, lastname, email, birthdate, gender):
        self.cursor.execute('''
        INSERT INTO Usuaris (name, lastname, email, birthdate, gender)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, lastname, email, birthdate, gender))
        self.conn.commit()

    def get_users(self):
        self.cursor.execute('SELECT name, lastname FROM Usuaris')
        return [{'name': row[0], 'lastname': row[1]} for row in self.cursor.fetchall()]

    def close(self):
        self.conn.close()
