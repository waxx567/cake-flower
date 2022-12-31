import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Query database
c.execute("SELECT * FROM test")
# c.fetchone() to get last added
# c.fetchmany(3) to fetch last 3 or whatever
print(c.fetchall())

# Commit command
conn.commit()

# Close connection
conn.close()
