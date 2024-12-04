DROP TABLE IF EXISTS Usuaris;
DROP TABLE IF EXISTS Dietes;

CREATE TABLE Pacients (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
	nom TEXT NOT NULL,
	cognoms TEXT NOT NULL,
	email TEXT NOT NULL,
	data_neixement DATE NOT NULL,
	sexe TEXT CHECK(sexe IN ('HOME', 'DONA'))
);

CREATE TABLE Mesures (
	mesures_id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE Dietes (
	diet_id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_id INTEGER,
	start_date DATE NOT NULL,
	end_date DATE,
	description TEXT,
	FOREIGN KEY (user_id) REFERENCES Pacients(user_id)
);

