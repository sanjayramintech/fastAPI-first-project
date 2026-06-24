import sqlite3

conn = sqlite3.connect("texts.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS texts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    tokens INTEGER NOT NULL,
    cost REAL NOT NULL
)
""")






cursor.execute("""
INSERT INTO texts (text, tokens, cost)
VALUES
('I love FastAPI', 4, 0.000008)
""")

cursor.execute("""
INSERT INTO texts (text, tokens, cost)
VALUES
('Python is easy', 3, 0.000006)
""")

conn.commit()
conn.close()
print("Database created successfully.")