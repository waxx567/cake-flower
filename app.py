import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")

# Create cursor
c = conn.cursor()

# Query database
# To find out the row id of the table
c.execute("SELECT rowid, * FROM test")

# Loop
items = c.fetchall()

for item in items:
    # Pulls elements out of tuples
    print(item)


# Commit command
conn.commit()

# Close connection
conn.close()
