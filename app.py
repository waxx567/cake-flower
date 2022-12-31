import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Query database
c.execute("SELECT * FROM test")

# Prints the first tuple when input of python app.py
print(c.fetchone())

# Commit command
conn.commit()

# Close connection
conn.close()
