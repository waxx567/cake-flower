import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Insert many records into db
c.execute()

# Commit command
conn.commit()

# Close connection
conn.close()
