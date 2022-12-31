import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Query database
c.execute("SELECT * FROM test")

# Print all
print(c.fetchall())

# Commit command
conn.commit()

# Close connection
conn.close()
