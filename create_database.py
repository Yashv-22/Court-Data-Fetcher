import sqlite3

# Connect to SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('court_data.db')

# Create a cursor object
c = conn.cursor()

# Create the queries table
c.execute('''
    CREATE TABLE IF NOT EXISTS queries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_type TEXT NOT NULL,
        case_number TEXT NOT NULL,
        filing_year INTEGER NOT NULL,
        response TEXT NOT NULL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
