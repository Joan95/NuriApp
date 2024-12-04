DROP TABLE IF EXISTS Usuaris;

CREATE TABLE Usuaris (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
	name TEXT NOT NULL,
	lastname TEXT NOT NULL,
	email TEXT,
	birthdate DATE,
	gender TEXT CHECK(gender IN ('MALE', 'FEMALE'))
);

CREATE TABLE Dietes(
	diet_id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_id INTEGER,
	start_date DATE NOT NULL,
	end_date DATE,
	description TEXT,
	FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

