import sqlite3

with open('schema.sql', 'r') as f:
    schema = f.read()

conn = sqlite3.connect('court_data.db')
conn.executescript(schema)
conn.commit()
conn.close()

print("Database initialized successfully.")
