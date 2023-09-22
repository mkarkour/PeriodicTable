import sqlite3

dbase = sqlite3.connect('mendeleev.db', isolation_level=None)
print('Database opened')
dbase.execute("PRAGMA foreign_keys = 1")

dbase.execute(''' CREATE TABLE IF NOT EXISTS Element (
    Nombre_atomique INTEGER PRIMARY KEY NOT NULL,
    Name TEXT NOT NULL,
    Symbole TEXT NOT NULL,
    Masse_atomique FLOAT NOT NULL,
    Electronegativite FLOAT,
    Electron_orbitale TEXT NOT NULL,
    Electron_couche TEXT
    ) ''')
print("Element table created successfully")

dbase.close()
print("Database closed")