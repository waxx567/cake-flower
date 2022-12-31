import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Insert one record into db
c.execute("INSERT INTO test VALUES ('Hal', 'Bell', 701)")

# Commit command
conn.commit()

# Close connection
conn.close()
