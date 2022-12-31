import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE test (
    first_name TEXT,
    last_name TEXT,
    number INTEGER
)""")

# Commit command
conn.commit()

# Close connection
conn.close()
