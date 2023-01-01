import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Query database
c.execute("SELECT rowid, * FROM test ORDER BY number")

items = c.fetchall()

# Loop through all
for item in items:
    print(item)

# Commit command
conn.commit()

# Close connection
conn.close()
